"""Card browser tab implementation."""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from tkinter import filedialog
from tkinter import ttk

import customtkinter as ctk
from PIL import Image, ImageOps

from forge_content_manager.constants import RARITY_LABELS
from forge_content_manager.models import CardRecord, ForgeSetRecord
from forge_content_manager.services.content_service import ForgeContentService
from forge_content_manager.ui.dialogs import confirm_action, show_error, show_info


class CardBrowserTab(ctk.CTkFrame):
    """Browse, edit, replace, and delete installed custom cards."""

    def __init__(self, master: ctk.CTkBaseClass, content_service: ForgeContentService, on_cards_changed: Callable[[], None]) -> None:
        """Build the browser layout with a card table and script editor."""
        super().__init__(master)
        self._content_service = content_service
        self._on_cards_changed = on_cards_changed
        self._records: dict[str, CardRecord] = {}
        self._sets: list[ForgeSetRecord] = []
        self._editor_image_source: Path | None = None
        self._editor_original_script = ""
        self._editor_original_rarity = ""

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        toolbar = ctk.CTkFrame(self)
        toolbar.grid(row=0, column=0, columnspan=2, sticky="ew", padx=16, pady=(16, 8))
        self.toolbar = toolbar
        toolbar.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(toolbar, text="Set:").grid(row=0, column=1, padx=(12, 4), pady=12)
        self.set_menu = ctk.CTkOptionMenu(toolbar, values=["All Sets"], command=lambda _value: self.refresh())
        self.set_menu.grid(row=0, column=2, padx=4, pady=12)
        ctk.CTkLabel(toolbar, text="Content:").grid(row=0, column=3, padx=(12, 4), pady=12)
        self.content_type_menu = ctk.CTkOptionMenu(toolbar, values=["Cards and Tokens", "Cards", "Tokens"], command=lambda _value: self.refresh())
        self.content_type_menu.grid(row=0, column=4, padx=4, pady=12)
        ctk.CTkLabel(toolbar, text="Rarity:").grid(row=0, column=5, padx=(12, 4), pady=12)
        self.filter_rarity_menu = ctk.CTkOptionMenu(toolbar, values=["All Rarities", *RARITY_LABELS], command=lambda _value: self.refresh())
        self.filter_rarity_menu.grid(row=0, column=6, padx=4, pady=12)
        ctk.CTkLabel(toolbar, text="Name:").grid(row=0, column=7, padx=(12, 4), pady=12)
        self.name_filter = ctk.CTkEntry(toolbar, placeholder_text="Filter cards")
        self.name_filter.grid(row=0, column=8, padx=4, pady=12, sticky="ew")
        self.name_filter.bind("<KeyRelease>", lambda _event: self.refresh())
        ctk.CTkButton(toolbar, text="Refresh", command=self.refresh, width=90).grid(row=0, column=9, padx=(8, 12), pady=12)

        table_frame = ctk.CTkFrame(self)
        table_frame.grid(row=1, column=0, sticky="nsew", padx=(16, 8), pady=(0, 16))
        table_frame.grid_columnconfigure(0, weight=1)
        table_frame.grid_rowconfigure(0, weight=1)

        columns = ("content_type", "name", "set_name", "rarity", "script_path", "image_present")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")
        headings = {
            "content_type": "Type",
            "name": "Card Name",
            "set_name": "Set",
            "rarity": "Rarity",
            "script_path": "Script File Path",
            "image_present": "Image Present",
        }
        widths = {"content_type": 80, "name": 180, "set_name": 180, "rarity": 100, "script_path": 360, "image_present": 110}
        for column in columns:
            self.tree.heading(column, text=headings[column])
            self.tree.column(column, width=widths[column], anchor="w")
        self.tree.grid(row=0, column=0, sticky="nsew")
        self.tree.bind("<<TreeviewSelect>>", self._handle_selection_changed)
        self.tree.bind("<ButtonRelease-1>", self._handle_click)

        table_scroll = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        table_scroll.grid(row=0, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=table_scroll.set)

        self.table_frame = table_frame
        self.editor_frame = ctk.CTkFrame(self)
        editor_frame = self.editor_frame
        editor_frame.grid_columnconfigure(0, weight=1)
        editor_frame.grid_rowconfigure(1, weight=1)
        editor_frame.grid_rowconfigure(2, weight=1)

        self.selection_label = ctk.CTkLabel(
            editor_frame,
            text="Select a card...",
            font=ctk.CTkFont(size=15, weight="bold"),
        )
        self.selection_label.grid(row=0, column=0, sticky="w", padx=12, pady=(12, 8))

        editor_controls = ctk.CTkFrame(editor_frame, fg_color="transparent")
        editor_controls.grid(row=3, column=0, sticky="ew", padx=12, pady=(0, 12))
        self.rarity_menu = ctk.CTkOptionMenu(editor_controls, values=list(RARITY_LABELS))
        self.rarity_menu.pack(side="left")
        ctk.CTkButton(editor_controls, text="Replace Image", command=self.replace_image, width=120).pack(side="left", padx=8)
        ctk.CTkButton(editor_controls, text="Save Changes", command=self.save_changes, width=120).pack(side="right")
        ctk.CTkButton(editor_controls, text="Back", command=self.show_table, width=90).pack(side="right", padx=8)

        self.editor_frame.grid_remove()

        self.script_editor = ctk.CTkTextbox(editor_frame, wrap="none", activate_scrollbars=True)
        self.script_editor.grid(row=1, column=0, sticky="nsew", padx=12, pady=(0, 6))

        self.image_preview = ctk.CTkLabel(editor_frame, text="No image available")
        self.image_preview.grid(row=2, column=0, sticky="nsew", padx=12, pady=(6, 12))
        self._image_preview: ctk.CTkImage | None = None
        self._image_preview_cache: dict[Path, tuple[int, ctk.CTkImage]] = {}

        self.refresh()

    def show_editor(self, record: CardRecord | None = None) -> None:
        """Show the editor for the selected card."""
        record = record or self._selected_record()
        if record is None:
            return
        self.table_frame.grid_remove()
        self.toolbar.grid_remove()
        self.editor_frame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=16, pady=16)
        self._handle_selection_changed(None)

    def show_table(self) -> None:
        """Return to the filtered card table."""
        if self.has_unsaved_changes() and not confirm_action("Unsaved Changes", "Discard your unsaved card changes?"):
            return
        self.editor_frame.grid_remove()
        self.toolbar.grid()
        self.table_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=16, pady=(0, 16))
        self.refresh()

    def refresh(self, selected_script_path: Path | None = None) -> None:
        """Reload the custom card scan results while keeping the current card selected."""
        if selected_script_path is None:
            selection = self.tree.selection()
            if selection:
                selected_record = self._records.get(selection[0])
                selected_script_path = selected_record.script_path if selected_record is not None else None
        self._clear_image_preview()
        self._records.clear()
        for item in self.tree.get_children():
            self.tree.delete(item)
        self._sets = self._content_service.list_sets()
        labels = ["All Sets", *[f"{item.name} [{item.code}]" for item in self._sets]]
        current = self.set_menu.get()
        self.set_menu.configure(values=labels)
        self.set_menu.set(current if current in labels else "All Sets")
        selected_label = self.set_menu.get()
        selected_set = next((item for item in self._sets if selected_label == f"{item.name} [{item.code}]"), None)
        rarity_filter = self.filter_rarity_menu.get()
        content_filter = self.content_type_menu.get()
        name_filter = self.name_filter.get().strip().casefold()
        for record in self._content_service.scan_cards():
            if content_filter == "Cards" and record.content_type != "card":
                continue
            if content_filter == "Tokens" and record.content_type != "token":
                continue
            if selected_set is not None and selected_set.name not in record.set_name.split(", "):
                continue
            if name_filter and name_filter not in record.name.casefold():
                continue
            rarity = self._rarity_for_record(record, selected_set) if record.content_type == "card" else "—"
            if rarity_filter != "All Rarities" and rarity != rarity_filter:
                continue
            item_id = f"{record.content_type}:{record.script_path}"
            self._records[item_id] = record
            self.tree.insert(
                "",
                "end",
                iid=item_id,
                values=(record.content_type.title(), record.name, record.set_name, rarity, str(record.script_path), "Yes" if record.image_present else "No"),
            )
        if selected_script_path is not None:
            item_id = next((key for key, record in self._records.items() if record.script_path == selected_script_path), None)
            if item_id:
                self.tree.selection_set(item_id)
                self.tree.focus(item_id)

    def _handle_click(self, _event) -> None:
        """Open the clicked card in the editor."""
        if self.tree.selection():
            self.show_editor()

    def open_selected_script(self) -> None:
        """Load the selected script into the in-app editor."""
        record = self._selected_record()
        if record is None:
            return
        script_text = self._content_service.load_script(record.script_path)
        self.script_editor.delete("1.0", "end")
        self.script_editor.insert("1.0", script_text)
        self.selection_label.configure(text=f"Editing: {record.name}")

    def save_selected_script(self) -> None:
        """Persist the edited script back to disk through the content service."""
        record = self._selected_record()
        if record is None:
            return
        new_text = self.script_editor.get("1.0", "end").rstrip()
        if not new_text:
            show_error("Empty Script", "The script editor cannot be empty.")
            return
        try:
            updated_record = self._content_service.save_script(record, new_text)
        except Exception as exc:
            show_error("Save Failed", str(exc))
            return
        show_info("Script Saved", f"Saved script for '{updated_record.name}'.")
        self.refresh(selected_script_path=updated_record.script_path)
        self._on_cards_changed()

    def replace_image(self) -> None:
        """Prompt for a new image and replace the selected card art."""
        record = self._selected_record()
        if record is None:
            return
        file_name = filedialog.askopenfilename(
            title="Choose Replacement Image",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.webp;*.bmp")],
        )
        if not file_name:
            return
        self._editor_image_source = Path(file_name)
        self.image_preview.configure(text=f"New image selected: {self._editor_image_source.name}")

    def save_changes(self) -> None:
        """Save the script, rarity, and optional replacement image together."""
        record = self._selected_record()
        if record is None:
            return
        new_text = self.script_editor.get("1.0", "end").rstrip()
        if not new_text:
            show_error("Empty Script", "The script editor cannot be empty.")
            return
        label = self.set_menu.get()
        selected = next((item for item in self._sets if label == f"{item.name} [{item.code}]"), None)
        if selected is None:
            show_error("Set Required", "Choose a specific set before saving changes.")
            return
        try:
            updated = self._content_service.save_script(record, new_text)
            if updated.content_type == "card":
                self._content_service.update_card_rarity(selected.file_path, updated.name, self.rarity_menu.get())
            if self._editor_image_source is not None:
                self._content_service.replace_image(updated, self._editor_image_source)
        except Exception as exc:
            show_error("Save Failed", str(exc))
            return
        self._editor_image_source = None
        self._editor_original_script = new_text
        self._editor_original_rarity = self.rarity_menu.get()
        self._on_cards_changed()
        self.show_table()

    def delete_selected_card(self) -> None:
        """Delete the selected card and update any edition references."""
        record = self._selected_record()
        if record is None:
            return
        if not confirm_action("Delete Card", f"Delete custom card '{record.name}'?"):
            return
        try:
            self._content_service.delete_card(record)
        except Exception as exc:
            show_error("Delete Failed", str(exc))
            return
        self.script_editor.delete("1.0", "end")
        self.selection_label.configure(text="Select a card to view or edit its Forge script.")
        self._clear_image_preview()
        self._on_cards_changed()
        show_info("Card Deleted", f"Deleted '{record.name}'.")

    def _selected_record(self) -> CardRecord | None:
        """Return the currently selected card record from the table."""
        selection = self.tree.selection()
        if not selection:
            show_error("Selection Required", "Select a card first.")
            return None
        return self._records.get(selection[0])

    def _handle_selection_changed(self, _event) -> None:
        """Keep the editor synchronized with the current table selection."""
        selection = self.tree.selection()
        if not selection:
            return
        record = self._records.get(selection[0])
        if record is None:
            return
        self.script_editor.delete("1.0", "end")
        script_text = self._content_service.load_script(record.script_path)
        self.script_editor.insert("1.0", script_text)
        self.selection_label.configure(text=f"Editing: {record.name}")
        if record.content_type == "token":
            self.rarity_menu.configure(state="disabled")
            self.rarity_menu.set("Common")
        else:
            self.rarity_menu.configure(state="normal")
            self._update_rarity(record)
        self._editor_original_script = script_text.rstrip()
        self._editor_original_rarity = self.rarity_menu.get()
        self._editor_image_source = None
        self._update_image_preview(record)

    def has_unsaved_changes(self) -> bool:
        """Return whether the open editor contains changes not yet saved."""
        return bool(
            self._editor_image_source is not None
            or self.script_editor.get("1.0", "end").rstrip() != self._editor_original_script
            or self.rarity_menu.get() != self._editor_original_rarity
        )

    def _rarity_for_record(self, record: CardRecord, selected_set: ForgeSetRecord | None) -> str:
        """Resolve rarity for the active set, or the first matching set."""
        if record.content_type == "token":
            return ""
        target = selected_set or next((item for item in self._sets if item.name in record.set_name.split(", ")), None)
        return self._content_service.get_card_rarity(target.file_path, record.name) if target else ""

    def _update_rarity(self, record: CardRecord) -> None:
        label = self.set_menu.get()
        selected = next((item for item in self._sets if label == f"{item.name} [{item.code}]"), None)
        if selected is None:
            selected = next((item for item in self._sets if item.name in record.set_name.split(", ")), None)
        if selected:
            self.rarity_menu.set(self._content_service.get_card_rarity(selected.file_path, record.name))

    def save_selected_rarity(self) -> None:
        record = self._selected_record()
        if record is None:
            return
        label = self.set_menu.get()
        selected = next((item for item in self._sets if label == f"{item.name} [{item.code}]"), None)
        if selected is None:
            show_error("Set Required", "Choose a specific set before saving rarity.")
            return
        try:
            self._content_service.update_card_rarity(selected.file_path, record.name, self.rarity_menu.get())
        except Exception as exc:
            show_error("Rarity Update Failed", str(exc))
            return
        self.refresh(selected_script_path=record.script_path)
        self._on_cards_changed()
        show_info("Rarity Updated", f"Updated '{record.name}' to {self.rarity_menu.get()}.")

    def _clear_image_preview(self) -> None:
        """Remove the currently displayed card image."""
        self._image_preview = None
        self.image_preview.configure(image=None, text="No image available")

    def _update_image_preview(self, record: CardRecord) -> None:
        """Display a scaled preview when the selected card has an image."""
        self._clear_image_preview()
        if record.image_path is None or not record.image_path.exists():
            return
        try:
            image_mtime = record.image_path.stat().st_mtime_ns
            cached_preview = self._image_preview_cache.get(record.image_path)
            if cached_preview is None or cached_preview[0] != image_mtime:
                with Image.open(record.image_path) as source_image:
                    preview_image = ImageOps.contain(source_image.convert("RGB"), (260, 360), Image.Resampling.LANCZOS)
                self._image_preview_cache[record.image_path] = (
                    image_mtime,
                    ctk.CTkImage(
                        light_image=preview_image,
                        dark_image=preview_image,
                        size=preview_image.size,
                    ),
                )
            self._image_preview = self._image_preview_cache[record.image_path][1]
        except (OSError, ValueError):
            self.image_preview.configure(text="Unable to load image")
            return
        self.image_preview.configure(image=self._image_preview, text="")
