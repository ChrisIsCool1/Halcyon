"""Card browser tab implementation."""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from tkinter import filedialog
from tkinter import ttk

import customtkinter as ctk
from PIL import Image, ImageOps

from forge_content_manager.constants import RARITY_CODES, RARITY_LABELS
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
        self._editor_art_index = 1
        self._editor_face_index = 0
        self._editor_image_is_alternate_art = False
        self._editor_selected_art_label = ""
        self._art_gallery_items: list[tuple[str, ctk.CTkFrame]] = []
        self._art_entry_paths: list[Path | None] = []
        self._fullscreen_window: ctk.CTkToplevel | None = None
        self._fullscreen_image: ctk.CTkImage | None = None
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
        self.flip_button = ctk.CTkButton(editor_controls, text="Show Back", command=self.flip_card, width=100)
        self.flip_button.pack(side="left", padx=(8, 0))
        self.flip_button.pack_forget()
        self.face_menu = ctk.CTkOptionMenu(editor_controls, values=["Card Art"], command=lambda _value: self._update_image_target_for_selected_face())
        self.face_menu.pack(side="left", padx=(8, 0))
        self.replace_image_button = ctk.CTkButton(editor_controls, text="Replace Image", command=self.replace_image, width=140)
        self.replace_image_button.pack(side="left", padx=8)
        ctk.CTkButton(editor_controls, text="Upload Alternate Art", command=self.replace_alternate_art, width=150).pack(side="left", padx=8)
        self.delete_art_button = ctk.CTkButton(editor_controls, text="Delete Selected Art", command=self.delete_selected_art, width=150)
        self.delete_art_button.pack(side="left", padx=8)
        self.delete_art_button.pack_forget()
        ctk.CTkButton(editor_controls, text="Save Changes", command=self.save_changes, width=120).pack(side="right")
        ctk.CTkButton(editor_controls, text="Back", command=self.show_table, width=90).pack(side="right", padx=8)

        self.image_status = ctk.CTkLabel(editor_frame, text="", anchor="w")
        self.image_status.grid(row=4, column=0, sticky="ew", padx=12, pady=(0, 10))

        self.editor_frame.grid_remove()

        self.script_editor = ctk.CTkTextbox(editor_frame, wrap="none", activate_scrollbars=True)
        self.script_editor.grid(row=1, column=0, sticky="nsew", padx=12, pady=(0, 6))

        self.art_gallery = ctk.CTkScrollableFrame(editor_frame, orientation="horizontal", height=215, label_text="Card Art")
        self.art_gallery.grid(row=2, column=0, sticky="ew", padx=12, pady=(6, 10))
        self._art_gallery_images: list[ctk.CTkImage] = []

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
        self._clear_image_status()
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

    def replace_image(self, *, title: str = "Choose Replacement Image", status_label: str = "Replacement selected") -> None:
        """Prompt for a new image and replace the selected card art."""
        record = self._selected_record()
        if record is None:
            return
        file_name = filedialog.askopenfilename(
            title=title,
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.webp;*.bmp")],
        )
        if not file_name:
            return
        self._editor_image_source = Path(file_name)
        self._editor_image_is_alternate_art = False
        self.image_status.configure(text=f"{status_label}: {self._editor_image_source.name}")

    def replace_alternate_art(self) -> None:
        """Select an alternate art image for the current card."""
        record = self._selected_record()
        if record is None or record.content_type != "card":
            return
        if self._editor_face_index != 0:
            show_error("Front Face Required", "Flip to the front face before uploading a new alternate art print.")
            return
        previous_source = self._editor_image_source
        previous_is_alternate = self._editor_image_is_alternate_art
        self.replace_image(title="Choose Alternate Art", status_label="New art uploaded")
        if self._editor_image_source is not None and self._editor_image_source != previous_source:
            self._editor_image_is_alternate_art = True
        elif self._editor_image_source == previous_source:
            self._editor_image_is_alternate_art = previous_is_alternate

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
                if self._editor_image_is_alternate_art:
                    self._content_service.replace_alternate_art(
                        updated,
                        self._editor_image_source,
                        selected.file_path,
                        RARITY_CODES[self.rarity_menu.get()],
                    )
                else:
                    self._content_service.replace_card_art_entry(
                        updated, self._editor_image_source, self._editor_art_index, self._editor_face_index
                    )
        except Exception as exc:
            show_error("Save Failed", str(exc))
            return
        self._editor_image_source = None
        self._editor_image_is_alternate_art = False
        self.image_status.configure(text="")
        self._editor_original_script = new_text
        self._editor_original_rarity = self.rarity_menu.get()
        self._on_cards_changed()
        self.show_table()

    def delete_selected_art(self) -> None:
        """Remove the selected art entry and its indexed image files."""
        record = self._selected_record()
        if record is None:
            return
        set_record = next((item for item in self._sets if item.code == record.set_code), None)
        if set_record is None:
            show_error("Set Required", "The selected card's edition file could not be found.")
            return
        label = self._editor_selected_art_label or record.name
        if not confirm_action("Delete Card Art", f"Delete art entry '{label}' for '{record.name}'?"):
            return
        try:
            self._content_service.delete_card_art_entry(record, set_record.file_path, self._editor_art_index)
        except Exception as exc:
            show_error("Delete Failed", str(exc))
            return
        self._editor_image_source = None
        self._editor_image_is_alternate_art = False
        self.image_status.configure(text="")
        labels = self._content_service.get_card_art_labels(record)
        self._editor_art_index = min(self._editor_art_index, len(labels))
        self._editor_selected_art_label = labels[self._editor_art_index - 1]
        self.face_menu.configure(values=labels)
        self.face_menu.set(self._editor_selected_art_label)
        self._update_art_gallery(record)
        self._on_cards_changed()

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
        self._clear_image_status()
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
        self._editor_art_index = 1
        self._editor_face_index = 0
        self._editor_image_is_alternate_art = False
        labels = self._content_service.get_card_art_labels(record)
        self._editor_selected_art_label = labels[0]
        self.face_menu.configure(values=labels)
        self.face_menu.set(labels[0])
        self.image_status.configure(text="")
        self._update_art_gallery(record)

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

    def _clear_image_status(self) -> None:
        """Clear any pending image replacement status."""
        self.image_status.configure(text="")

    def _update_art_gallery(self, record: CardRecord) -> None:
        """Display each print's image for the currently viewed card face."""
        for child in self.art_gallery.winfo_children():
            child.destroy()
        self._art_gallery_images.clear()
        self._art_gallery_items.clear()
        labels = self._content_service.get_card_art_labels(record)
        faces = record.face_names or [record.name]
        has_back = len(faces) > 1
        self._editor_face_index = min(self._editor_face_index, len(faces) - 1)
        if has_back:
            self.flip_button.pack(side="left", padx=(8, 0), before=self.face_menu)
            viewing_back = self._editor_face_index > 0
            self.flip_button.configure(text="Show Front" if viewing_back else "Show Back")
            self.replace_image_button.configure(text="Replace Back Image" if viewing_back else "Replace Front Image")
        else:
            self.flip_button.pack_forget()
            self._editor_face_index = 0
            self.replace_image_button.configure(text="Replace Image")
        self._art_entry_paths = self._content_service.get_card_art_entry_paths(record, self._editor_face_index)
        self.art_gallery.configure(label_text=f"{faces[self._editor_face_index]} Art")
        self.face_menu.configure(values=labels)
        if self._editor_selected_art_label not in labels:
            self._editor_art_index = 1
            self._editor_selected_art_label = labels[0]
        self.face_menu.set(self._editor_selected_art_label)
        if len(labels) > 1:
            self.delete_art_button.pack(side="left", padx=8)
        else:
            self.delete_art_button.pack_forget()
        for art_index, art_label in enumerate(labels, start=1):
            path = self._art_entry_paths[art_index - 1] if art_index <= len(self._art_entry_paths) else None
            item = ctk.CTkFrame(
                self.art_gallery,
                cursor="hand2",
                border_width=2 if len(labels) > 1 and art_label == self._editor_selected_art_label else 0,
                border_color="#77C8FF",
            )
            item.pack(side="left", padx=6, pady=6)
            self._art_gallery_items.append((art_label, item))
            image_label = None
            if path is not None and path.exists():
                try:
                    with Image.open(path) as source_image:
                        preview = ImageOps.contain(source_image.convert("RGB"), (125, 175), Image.Resampling.LANCZOS)
                    art_image = ctk.CTkImage(light_image=preview, dark_image=preview, size=preview.size)
                    self._art_gallery_images.append(art_image)
                    image_label = ctk.CTkLabel(item, image=art_image, text="", cursor="hand2")
                except (OSError, ValueError):
                    pass
            if image_label is None:
                image_label = ctk.CTkLabel(item, text="No image", width=125, height=175, cursor="hand2")
            image_label.pack(padx=5, pady=(5, 2))
            text_label = ctk.CTkLabel(item, text=art_label, cursor="hand2")
            text_label.pack(padx=5, pady=(0, 5))
            select_art = lambda _event=None, label=art_label, index=art_index: self._select_gallery_art(label, index)
            for widget in (item, image_label, text_label):
                widget.bind("<Button-1>", select_art)
            if path is not None and path.exists():
                show_fullscreen = lambda _event=None, image_path=path: self._open_art_fullscreen(image_path)
                image_label.bind("<Double-Button-1>", show_fullscreen)
                item.bind("<Double-Button-1>", show_fullscreen)
        self._refresh_gallery_selection()

    def flip_card(self) -> None:
        """Switch the displayed card face while keeping the selected print."""
        selection = self.tree.selection()
        record = self._records.get(selection[0]) if selection else None
        if record is None or len(record.face_names) < 2:
            return
        self._editor_face_index = 1 - self._editor_face_index
        self.image_status.configure(text="")
        self._update_art_gallery(record)

    def _select_gallery_art(self, label: str, art_index: int) -> None:
        """Select a gallery tile as the replacement and deletion target."""
        self._editor_art_index = art_index
        self._editor_image_is_alternate_art = False
        self._editor_selected_art_label = label
        self.face_menu.set(label)
        self._refresh_gallery_selection()

    def _refresh_gallery_selection(self) -> None:
        """Draw a light blue border around the selected thumbnail when choices exist."""
        show_border = len(self._art_gallery_items) > 1
        for label, item in self._art_gallery_items:
            item.configure(border_width=2 if show_border and label == self._editor_selected_art_label else 0)

    def _update_image_target_for_selected_face(self) -> None:
        """Synchronize the selected art index with the caption dropdown."""
        labels = self.face_menu.cget("values")
        selected_label = self.face_menu.get()
        if selected_label not in labels:
            return
        self._editor_art_index = list(labels).index(selected_label) + 1
        self._editor_selected_art_label = selected_label
        self._editor_image_is_alternate_art = False
        self._refresh_gallery_selection()

    def _open_art_fullscreen(self, image_path: Path) -> None:
        """Show a dimmed full-screen preview that closes on an outside click."""
        if self._fullscreen_window is not None and self._fullscreen_window.winfo_exists():
            self._fullscreen_window.destroy()
        window = ctk.CTkToplevel(self.winfo_toplevel())
        self._fullscreen_window = window
        window.overrideredirect(True)
        width, height = window.winfo_screenwidth(), window.winfo_screenheight()
        window.geometry(f"{width}x{height}+0+0")
        window.configure(fg_color="#101820")
        window.attributes("-alpha", 0.9)
        backdrop = ctk.CTkFrame(window, fg_color="transparent", corner_radius=0)
        backdrop.pack(fill="both", expand=True)
        backdrop.bind("<Button-1>", lambda _event: window.destroy())
        try:
            with Image.open(image_path) as source_image:
                preview = ImageOps.contain(
                    source_image.convert("RGB"),
                    (max(1, int(width * 0.84)), max(1, int(height * 0.88))),
                    Image.Resampling.LANCZOS,
                )
            self._fullscreen_image = ctk.CTkImage(light_image=preview, dark_image=preview, size=preview.size)
            image_label = ctk.CTkLabel(backdrop, image=self._fullscreen_image, text="", fg_color="transparent")
            image_label.place(relx=0.5, rely=0.5, anchor="center")
        except (OSError, ValueError) as exc:
            window.destroy()
            show_error("Image Preview Failed", str(exc))
            return
        window.bind("<Escape>", lambda _event: window.destroy())
        window.focus_force()
