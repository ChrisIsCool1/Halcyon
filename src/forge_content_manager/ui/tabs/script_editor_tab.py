"""Guided, non-validating editor for MTG Forge card scripts."""

from __future__ import annotations

from collections.abc import Callable
import re
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox

import customtkinter as ctk

from forge_content_manager.models import CardImportInput
from forge_content_manager.services.content_service import ForgeContentService
from forge_content_manager.services.script_authoring_service import ReferenceCard, ScriptAuthoringService, ScriptDocumentation
from forge_content_manager.ui.dialogs import show_error, show_info


class ScriptEditorTab(ctk.CTkFrame):
    """Draft Forge scripts with completion, highlighting, documentation, and references."""

    def __init__(
        self,
        master: ctk.CTkBaseClass,
        content_service: ForgeContentService,
        authoring_service: ScriptAuthoringService,
        on_import_complete: Callable[[], None],
    ) -> None:
        """Build the non-validating Forge script editor.

        Args:
            master: Parent CustomTkinter widget.
            content_service: Service used to list sets and import drafts.
            authoring_service: Completion, documentation, and reference provider.
            on_import_complete: Callback invoked after a successful import.
        """
        super().__init__(master)
        self._content_service = content_service
        self._authoring_service = authoring_service
        self._on_import_complete = on_import_complete
        self._draft_path: Path | None = None
        self._dirty = False
        self._completion: tk.Toplevel | None = None
        self._completion_items: list[ScriptDocumentation] = []
        self._completion_just_accepted = False
        self._reference_cards: list[ReferenceCard] = []

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(1, weight=1)

        # Build the toolbar with draft management buttons, set selection, and status.
        toolbar = ctk.CTkFrame(self)
        toolbar.grid(row=0, column=0, columnspan=2, sticky="ew", padx=16, pady=(16, 8))
        toolbar.grid_columnconfigure(6, weight=1)
        for column, (text, command) in enumerate((("New", self.new_draft), ("Open", self.open_draft), ("Save", self.save_draft), ("Save As", self.save_draft_as))):
            ctk.CTkButton(toolbar, text=text, command=command, width=85).grid(row=0, column=column, padx=(12 if column == 0 else 4, 4), pady=10)
        ctk.CTkButton(toolbar, text="Import into Set", command=self.import_draft, width=130).grid(row=0, column=4, padx=8, pady=10)
        self._set_menu = ctk.CTkOptionMenu(toolbar, values=["No sets available"], width=210)
        self._set_menu.grid(row=0, column=5, padx=4, pady=10)
        self._status = ctk.CTkLabel(toolbar, text="Untitled draft", anchor="e")
        self._status.grid(row=0, column=6, sticky="ew", padx=12)

        # Build the main editor frame with syntax highlighting and autocompletion.
        editor_frame = ctk.CTkFrame(self)
        editor_frame.grid(row=1, column=0, sticky="nsew", padx=(16, 8), pady=(0, 16))
        editor_frame.grid_columnconfigure(0, weight=1)
        editor_frame.grid_rowconfigure(1, weight=1)
        ctk.CTkLabel(editor_frame, text="Forge Script", font=ctk.CTkFont(size=18, weight="bold")).grid(row=0, column=0, sticky="w", padx=12, pady=(12, 6))
        self.editor = tk.Text(editor_frame, undo=True, wrap="none", font=("Cascadia Mono", 11), relief="flat", borderwidth=0)
        self.editor.grid(row=1, column=0, sticky="nsew", padx=(12, 0), pady=(0, 12))
        scroll = tk.Scrollbar(editor_frame, command=self.editor.yview)
        scroll.grid(row=1, column=1, sticky="ns", padx=(0, 12), pady=(0, 12))
        self.editor.configure(yscrollcommand=scroll.set)
        self._configure_tags()
        self.editor.bind("<KeyRelease>", self._handle_editor_change)
        self.editor.bind("<ButtonRelease-1>", self._handle_editor_change)
        self.editor.bind("<Tab>", self._accept_completion)
        self.editor.bind("<Return>", self._accept_completion)
        self.editor.bind("<Down>", lambda _event: self._move_completion(1))
        self.editor.bind("<Up>", lambda _event: self._move_completion(-1))
        self.editor.bind("<Escape>", lambda _event: self._close_completion())

        # Build the side frame with documentation and reference cards.
        side = ctk.CTkFrame(self)
        side.grid(row=1, column=1, sticky="nsew", padx=(8, 16), pady=(0, 16))
        side.grid_columnconfigure(0, weight=1)
        side.grid_rowconfigure(1, weight=2)
        side.grid_rowconfigure(4, weight=1)
        ctk.CTkLabel(side, text="Keyword Help", font=ctk.CTkFont(size=18, weight="bold")).grid(row=0, column=0, sticky="w", padx=12, pady=(12, 4))
        self.documentation = ctk.CTkTextbox(side, wrap="word", state="disabled")
        self.documentation.grid(row=1, column=0, sticky="nsew", padx=12, pady=(0, 10))
        ctk.CTkLabel(side, text="Reference Cards", font=ctk.CTkFont(size=16, weight="bold")).grid(row=2, column=0, sticky="w", padx=12, pady=(4, 4))
        self.reference_search = ctk.CTkEntry(side, placeholder_text="Search optional cardsfolder…")
        self.reference_search.grid(row=3, column=0, sticky="ew", padx=12, pady=(0, 5))
        self.reference_search.bind("<KeyRelease>", lambda _event: self._refresh_references())
        self.reference_list = tk.Listbox(side, height=8, exportselection=False)
        self.reference_list.grid(row=4, column=0, sticky="nsew", padx=12, pady=(0, 6))
        self.reference_list.bind("<<ListboxSelect>>", lambda _event: self._show_reference())
        reference_buttons = ctk.CTkFrame(side, fg_color="transparent")
        reference_buttons.grid(row=5, column=0, sticky="ew", padx=12, pady=(0, 12))
        ctk.CTkButton(reference_buttons, text="Copy Script", command=self.copy_reference, width=110).pack(side="left")
        self.reference_status = ctk.CTkLabel(reference_buttons, text="", anchor="e")
        self.reference_status.pack(side="right", fill="x", expand=True, padx=(8, 0))
        self.refresh_sets()
        self.refresh_reference_cards()

    def refresh_sets(self) -> None:
        """Reload destination set choices."""
        records = self._content_service.list_sets()
        values = [f"{record.name} [{record.code}]" for record in records] or ["No sets available"]
        self._set_menu.configure(values=values)
        if self._set_menu.get() not in values:
            self._set_menu.set(values[0])

    def new_draft(self) -> None:
        """Start an empty draft after guarding unsaved work."""
        if not self._confirm_discard():
            return
        self.editor.delete("1.0", "end")
        self._draft_path = None
        self._dirty = False
        self._update_status()
        self._highlight()

    def open_draft(self) -> None:
        """Open a standalone UTF-8 script draft."""
        if not self._confirm_discard():
            return
        file_name = filedialog.askopenfilename(title="Open Forge Script", filetypes=[("Forge Scripts", "*.txt"), ("All Files", "*.*")])
        if not file_name:
            return
        try:
            text = Path(file_name).read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            show_error("Open Failed", str(exc))
            return
        self.editor.delete("1.0", "end")
        self.editor.insert("1.0", text)
        self._draft_path = Path(file_name)
        self._dirty = False
        self._update_status()
        self._highlight()

    def save_draft(self) -> bool:
        """Save the current draft, prompting for its initial location."""
        if self._draft_path is None:
            return self.save_draft_as()
        try:
            self._draft_path.write_text(self.editor.get("1.0", "end-1c"), encoding="utf-8")
        except OSError as exc:
            show_error("Save Failed", str(exc))
            return False
        self._dirty = False
        self._update_status()
        return True

    def save_draft_as(self) -> bool:
        """Choose a new standalone UTF-8 draft location and save it."""
        file_name = filedialog.asksaveasfilename(title="Save Forge Script", defaultextension=".txt", filetypes=[("Forge Scripts", "*.txt")])
        if not file_name:
            return False
        self._draft_path = Path(file_name)
        return self.save_draft()

    def import_draft(self) -> None:
        """Import the draft as one card through the established content workflow."""
        records = self._content_service.list_sets()
        selected = next((record for record in records if self._set_menu.get() == f"{record.name} [{record.code}]"), None)
        if selected is None:
            show_error("Set Selection", "Create and select a destination set before importing.")
            return
        text = self.editor.get("1.0", "end-1c")
        if not text.strip():
            show_error("Missing Script", "Write a Forge script before importing.")
            return
        unresolved = self._authoring_service.unresolved_svar_references(text)
        if unresolved:
            details = ", ".join(f"{item.label}$ {item.value} (line {item.line_number})" for item in unresolved[:5])
            suffix = "" if len(unresolved) <= 5 else f", and {len(unresolved) - 5} more"
            if not messagebox.askyesno("Unresolved SVar references", f"These Execute/SubAbility values do not name an SVar: {details}{suffix}.\n\nImport anyway?"):
                return
        summary = self._content_service.import_cards(selected, [CardImportInput(text, None, "Common")])
        result = summary.results[0]
        if result.success:
            show_info("Script Imported", f"Imported '{result.card_name}' into {selected.name}." + (f"\nWarnings: {'; '.join(result.warnings)}" if result.warnings else ""))
            self._on_import_complete()
        else:
            show_error("Import Failed", result.error or "Forge rejected the script metadata.")

    def _handle_editor_change(self, _event=None) -> None:
        self._dirty = True
        self._update_status()
        self._highlight()
        token = self._current_token()
        line = self.editor.get("insert linestart", "insert lineend")
        cursor = len(self.editor.get("insert linestart", "insert"))
        self._update_documentation(self._authoring_service.lookup_context(line, cursor))
        if self._completion_just_accepted and _event is not None and _event.keysym in {"Return", "Tab"}:
            self._completion_just_accepted = False
            return
        if token and len(token) >= 2:
            self._show_completion(token)
        else:
            self._close_completion()

    def _configure_tags(self) -> None:
        self.editor.tag_configure("field", foreground="#4c9aff")
        self.editor.tag_configure("prefix", foreground="#c586c0")
        self.editor.tag_configure("mode", foreground="#4ec9b0")
        self.editor.tag_configure("parameter", foreground="#dcdcaa")
        self.editor.tag_configure("svar", foreground="#ce9178")
        self.editor.tag_configure("svar-reference", foreground="#569cd6", underline=True)
        self.editor.tag_configure("invalid-svar-reference", foreground="#f14c4c", underline=True)

    def _highlight(self) -> None:
        for tag in ("field", "prefix", "mode", "parameter", "svar", "svar-reference", "invalid-svar-reference"):
            self.editor.tag_remove(tag, "1.0", "end")
        text = self.editor.get("1.0", "end-1c")
        unresolved = {(item.line_number, item.start, item.end) for item in self._authoring_service.unresolved_svar_references(text)}
        for line_number, line in enumerate(text.splitlines(), start=1):
            for tag, pattern in (("field", r"^[A-Za-z][\w]*:"), ("prefix", r"\b(?:A|T|S|R|K|SVar):"), ("mode", r"\b(?:DB|SP|AB)\$\s*\w+"), ("parameter", r"\|\s*\w+\$"), ("svar", r"\bSVar:[\w-]+")):
                for match in re.finditer(pattern, line):
                    self.editor.tag_add(tag, f"{line_number}.{match.start()}", f"{line_number}.{match.end()}")
            for match in re.finditer(r"\|\s*(?:Execute|SubAbility)\$\s*([^|\r\n]+)", line):
                value_start = match.start(1) + len(match.group(1)) - len(match.group(1).lstrip())
                value_end = value_start + len(match.group(1).strip())
                tag = "invalid-svar-reference" if (line_number, value_start, value_end) in unresolved else "svar-reference"
                self.editor.tag_add(tag, f"{line_number}.{value_start}", f"{line_number}.{value_end}")

    def _current_token(self) -> str:
        before = self.editor.get("insert linestart", "insert")
        match = re.search(r"([A-Za-z][\w ]*)$", before)
        return match.group(1).strip() if match else ""

    def _show_completion(self, token: str) -> None:
        line = self.editor.get("insert linestart", "insert lineend")
        cursor = len(self.editor.get("insert linestart", "insert"))
        self._completion_items = self._authoring_service.complete_context(line, cursor, token)
        if not self._completion_items:
            self._close_completion()
            return
        if self._completion is None:
            self._completion = tk.Toplevel(self)
            self._completion.overrideredirect(True)
            self._completion.attributes("-topmost", True)
            self._completion_list = tk.Listbox(self._completion, height=8, exportselection=False)
            self._completion_list.pack(fill="both", expand=True)
            self._completion_list.bind("<Double-Button-1>", self._accept_completion)
            self._completion_list.bind("<Return>", self._accept_completion)
            self._completion_list.bind("<<ListboxSelect>>", self._update_completion_documentation)
        selection = self._completion_list.curselection()
        selected_name = self._completion_list.get(selection[0]) if selection else None
        self._completion_list.delete(0, "end")
        for item in self._completion_items:
            self._completion_list.insert("end", item.name)
        selected_index = next((index for index, item in enumerate(self._completion_items) if item.name == selected_name), 0)
        self._completion_list.selection_set(selected_index)
        self._completion_list.see(selected_index)
        self._update_documentation(self._completion_items[selected_index])
        bbox = self.editor.bbox("insert")
        if bbox:
            self._completion.geometry(f"300x160+{self.editor.winfo_rootx() + bbox[0]}+{self.editor.winfo_rooty() + bbox[1] + bbox[3]}")

    def _accept_completion(self, _event=None):
        if self._completion is None:
            return None
        selection = self._completion_list.curselection()
        if not selection:
            return "break"
        item = self._completion_items[selection[0]]
        token = self._current_token()
        self.editor.delete(f"insert-{len(token)}c", "insert")
        self.editor.insert("insert", item.name)
        self._update_documentation(item)
        self._completion_just_accepted = True
        self._close_completion()
        self._highlight()
        return "break"

    def _move_completion(self, delta: int):
        """Move the active popup choice without taking focus from the editor."""
        if self._completion is None:
            return None
        selection = self._completion_list.curselection()
        current = selection[0] if selection else 0
        target = max(0, min(current + delta, self._completion_list.size() - 1))
        self._completion_list.selection_clear(0, "end")
        self._completion_list.selection_set(target)
        self._completion_list.see(target)
        self._update_documentation(self._completion_items[target])
        return "break"

    def _update_completion_documentation(self, _event=None) -> None:
        """Show help for the popup's active option while completion is visible."""
        selection = self._completion_list.curselection()
        if selection:
            self._update_documentation(self._completion_items[selection[0]])

    def _close_completion(self):
        if self._completion is not None:
            self._completion.destroy()
            self._completion = None

    def _update_documentation(self, item: ScriptDocumentation | None) -> None:
        text = "Place the cursor on a recognized Forge term to view its help.\n\nCompletion suggestions appear after two characters."
        if item is not None:
            parts = [f"{item.category}\n{item.signature}", item.description or "No detailed description is available."]
            if item.example:
                parts.append(f"Example:\n{item.example}")
            text = "\n\n".join(parts)
        self.documentation.configure(state="normal")
        self.documentation.delete("1.0", "end")
        self.documentation.insert("1.0", text)
        self.documentation.configure(state="disabled")

    def _refresh_references(self) -> None:
        self.reference_status.configure(text=self._authoring_service.reference_status())
        self._reference_cards = self._authoring_service.search_reference_cards(self.reference_search.get())
        self.reference_list.delete(0, "end")
        for card in self._reference_cards:
            self.reference_list.insert("end", card.name)

    def refresh_reference_cards(self) -> None:
        """Refresh reference results and poll only while a database build is active."""
        self._refresh_references()
        if self._authoring_service.is_indexing:
            self.after(500, self._poll_reference_index)

    def _poll_reference_index(self) -> None:
        """Refresh the status and active search after asynchronous indexing completes."""
        self.refresh_reference_cards()

    def _show_reference(self) -> None:
        selection = self.reference_list.curselection()
        if not selection:
            return
        try:
            script = self._authoring_service.load_reference_card(self._reference_cards[selection[0]])
        except (OSError, UnicodeError) as exc:
            show_error("Reference Failed", str(exc))
            return
        window = ctk.CTkToplevel(self)
        window.title(f"Reference: {self._reference_cards[selection[0]].name}")
        window.geometry("820x620")
        window.grid_columnconfigure(0, weight=1)
        window.grid_rowconfigure(0, weight=1)
        preview = tk.Text(window, wrap="none", font=("Cascadia Mono", 11), state="normal")
        preview.grid(row=0, column=0, sticky="nsew", padx=12, pady=12)
        preview.insert("1.0", script)
        preview.configure(state="disabled")
        buttons = ctk.CTkFrame(window, fg_color="transparent")
        buttons.grid(row=1, column=0, sticky="e", padx=12, pady=(0, 12))
        ctk.CTkButton(buttons, text="Insert All", command=lambda: self._insert_reference_text(script)).pack(side="right")
        ctk.CTkButton(buttons, text="Insert Selection", command=lambda: self._insert_preview_selection(preview)).pack(side="right", padx=(0, 8))

    def copy_reference(self) -> None:
        """Insert the selected reference card script at the editor caret.

        If no reference is selected or the indexed script is unavailable, an
        error dialog is shown and the editor is left unchanged.
        """
        selection = self.reference_list.curselection()
        if not selection:
            show_error("Reference Selection", "Select a reference card first.")
            return
        try:
            script = self._authoring_service.load_reference_card(self._reference_cards[selection[0]])
        except (OSError, UnicodeError) as exc:
            show_error("Reference Failed", str(exc))
            return
        self._insert_reference_text(script)

    def _insert_preview_selection(self, preview: tk.Text) -> None:
        try:
            text = preview.get("sel.first", "sel.last")
        except tk.TclError:
            show_error("Reference Selection", "Select text in the reference script first.")
            return
        self._insert_reference_text(text)

    def _insert_reference_text(self, text: str) -> None:
        self.editor.insert("insert", text)
        self._handle_editor_change()

    def _confirm_discard(self) -> bool:
        if not self._dirty:
            return True
        answer = messagebox.askyesnocancel("Unsaved Draft", "Save changes to the current draft?")
        return False if answer is None else (self.save_draft() if answer else True)

    def _update_status(self) -> None:
        name = self._draft_path.name if self._draft_path else "Untitled draft"
        self._status.configure(text=f"{name}{' • modified' if self._dirty else ''}")
