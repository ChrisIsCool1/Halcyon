"""Card browser tab implementation."""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from tkinter import filedialog
from tkinter import ttk

import customtkinter as ctk
from PIL import Image, ImageOps

from forge_content_manager.models import CardRecord
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

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        toolbar = ctk.CTkFrame(self)
        toolbar.grid(row=0, column=0, columnspan=2, sticky="ew", padx=16, pady=(16, 8))
        toolbar.grid_columnconfigure(0, weight=1)

        refresh_button = ctk.CTkButton(toolbar, text="Refresh", command=self.refresh, width=100)
        refresh_button.grid(row=0, column=1, padx=8, pady=12)

        open_button = ctk.CTkButton(toolbar, text="Open Script", command=self.open_selected_script, width=120)
        open_button.grid(row=0, column=2, padx=8, pady=12)

        save_button = ctk.CTkButton(toolbar, text="Save Script", command=self.save_selected_script, width=120)
        save_button.grid(row=0, column=3, padx=8, pady=12)

        replace_button = ctk.CTkButton(toolbar, text="Replace Image", command=self.replace_image, width=120)
        replace_button.grid(row=0, column=4, padx=8, pady=12)

        delete_button = ctk.CTkButton(toolbar, text="Delete Card", command=self.delete_selected_card, width=120)
        delete_button.grid(row=0, column=5, padx=(8, 12), pady=12)

        table_frame = ctk.CTkFrame(self)
        table_frame.grid(row=1, column=0, sticky="nsew", padx=(16, 8), pady=(0, 16))
        table_frame.grid_columnconfigure(0, weight=1)
        table_frame.grid_rowconfigure(0, weight=1)

        columns = ("name", "set_name", "script_path", "image_present")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")
        headings = {
            "name": "Card Name",
            "set_name": "Set",
            "script_path": "Script File Path",
            "image_present": "Image Present",
        }
        widths = {"name": 200, "set_name": 220, "script_path": 420, "image_present": 110}
        for column in columns:
            self.tree.heading(column, text=headings[column])
            self.tree.column(column, width=widths[column], anchor="w")
        self.tree.grid(row=0, column=0, sticky="nsew")
        self.tree.bind("<<TreeviewSelect>>", self._handle_selection_changed)

        table_scroll = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        table_scroll.grid(row=0, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=table_scroll.set)

        editor_frame = ctk.CTkFrame(self)
        editor_frame.grid(row=1, column=1, sticky="nsew", padx=(8, 16), pady=(0, 16))
        editor_frame.grid_columnconfigure(0, weight=1)
        editor_frame.grid_rowconfigure(1, weight=1)
        editor_frame.grid_rowconfigure(2, weight=1)

        self.selection_label = ctk.CTkLabel(
            editor_frame,
            text="Select a card...",
            font=ctk.CTkFont(size=15, weight="bold"),
        )
        self.selection_label.grid(row=0, column=0, sticky="w", padx=12, pady=(12, 8))

        self.script_editor = ctk.CTkTextbox(editor_frame, wrap="none", activate_scrollbars=True)
        self.script_editor.grid(row=1, column=0, sticky="nsew", padx=12, pady=(0, 6))

        self.image_preview = ctk.CTkLabel(editor_frame, text="No image available")
        self.image_preview.grid(row=2, column=0, sticky="nsew", padx=12, pady=(6, 12))
        self._image_preview: ctk.CTkImage | None = None

        self.refresh()

    def refresh(self, selected_script_path: Path | None = None) -> None:
        """Reload the custom card scan results while keeping the current card selected."""
        if selected_script_path is None:
            selection = self.tree.selection()
            if selection:
                selected_script_path = Path(selection[0])
        self._clear_image_preview()
        self._records.clear()
        for item in self.tree.get_children():
            self.tree.delete(item)
        for record in self._content_service.scan_cards():
            item_id = str(record.script_path)
            self._records[item_id] = record
            self.tree.insert(
                "",
                "end",
                iid=item_id,
                values=(record.name, record.set_name, str(record.script_path), "Yes" if record.image_present else "No"),
            )
        if selected_script_path is not None and str(selected_script_path) in self._records:
            self.tree.selection_set(str(selected_script_path))
            self.tree.focus(str(selected_script_path))

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
        try:
            self._content_service.replace_image(record, Path(file_name))
        except Exception as exc:
            show_error("Replace Image Failed", str(exc))
            return
        self.refresh()
        show_info("Image Replaced", f"Replaced image for '{record.name}'.")

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
        self.script_editor.insert("1.0", self._content_service.load_script(record.script_path))
        self.selection_label.configure(text=f"Editing: {record.name}")
        self._update_image_preview(record)

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
            with Image.open(record.image_path) as source_image:
                preview_image = ImageOps.contain(source_image.convert("RGB"), (260, 360), Image.Resampling.LANCZOS)
            self._image_preview = ctk.CTkImage(
                light_image=preview_image,
                dark_image=preview_image,
                size=preview_image.size,
            )
        except (OSError, ValueError):
            self.image_preview.configure(text="Unable to load image")
            return
        self.image_preview.configure(image=self._image_preview, text="")
