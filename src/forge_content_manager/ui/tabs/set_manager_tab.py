"""Set management tab implementation."""

from __future__ import annotations

from datetime import date
from pathlib import Path
from tkinter import filedialog

import customtkinter as ctk
from tkinter import ttk

from forge_content_manager.services.content_service import ForgeContentService
from forge_content_manager.ui.dialogs import SetMetadataDialog, confirm_action, show_error, show_info


class SetManagerTab(ctk.CTkFrame):
    """Display and manage Forge custom set edition files."""

    def __init__(self, master: ctk.CTkBaseClass, content_service: ForgeContentService, on_sets_changed: callable) -> None:
        """Build the set manager layout and initial controls."""
        super().__init__(master)
        self._content_service = content_service
        self._on_sets_changed = on_sets_changed
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        toolbar = ctk.CTkFrame(self)
        toolbar.grid(row=0, column=0, sticky="ew", padx=16, pady=(16, 8))
        for column in range(5):
            toolbar.grid_columnconfigure(column, weight=0)
        toolbar.grid_columnconfigure(5, weight=1)

        buttons = [
            ("Create Set", self._create_set),
            ("Edit Metadata", self._edit_set),
            ("Rename Set", self._rename_set),
            ("Delete Set", self._delete_set),
            ("Export Package", self._export_set),
            ("Import Package", self._import_package),
        ]
        for column, (label, command) in enumerate(buttons):
            button = ctk.CTkButton(toolbar, text=label, command=command, width=130)
            button.grid(row=0, column=column, padx=8, pady=12)

        tree_frame = ctk.CTkFrame(self)
        tree_frame.grid(row=1, column=0, sticky="nsew", padx=16, pady=(0, 16))
        tree_frame.grid_columnconfigure(0, weight=1)
        tree_frame.grid_rowconfigure(0, weight=1)

        columns = ("name", "code", "date", "card_count", "path")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=20)
        headings = {
            "name": "Set Name",
            "code": "Set Code",
            "date": "Date",
            "card_count": "Card Count",
            "path": "Edition File",
        }
        widths = {"name": 220, "code": 120, "date": 120, "card_count": 100, "path": 420}
        for column in columns:
            self.tree.heading(column, text=headings[column])
            self.tree.column(column, width=widths[column], anchor="w")
        self.tree.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=scrollbar.set)

    def refresh(self) -> None:
        """Reload the set list from the Forge filesystem."""
        for item in self.tree.get_children():
            self.tree.delete(item)
        for set_record in self._content_service.list_sets():
            self.tree.insert(
                "",
                "end",
                iid=str(set_record.file_path),
                values=(set_record.name, set_record.code, set_record.date, set_record.card_count, str(set_record.file_path)),
            )

    def _selected_set(self):
        """Return the selected set record or None when nothing is selected."""
        selection = self.tree.selection()
        if not selection:
            show_error("Selection Required", "Select a set first.")
            return None
        file_path = Path(selection[0])
        for set_record in self._content_service.list_sets():
            if set_record.file_path == file_path:
                return set_record
        show_error("Set Not Found", "The selected set no longer exists.")
        return None

    def _create_set(self) -> None:
        """Prompt for set metadata and create a new Forge edition file."""
        dialog = SetMetadataDialog(self, "Create Set", initial_values={"date": date.today().isoformat(), "type": "Custom"})
        self.wait_window(dialog)
        if not dialog.result:
            return
        try:
            self._content_service.create_set(
                name=dialog.result["name"],
                code=dialog.result["code"],
                date_value=dialog.result["date"],
                set_type=dialog.result["type"],
            )
        except Exception as exc:
            show_error("Create Set Failed", str(exc))
            return
        self._on_sets_changed()
        show_info("Set Created", f"Created set '{dialog.result['name']}'.")

    def _edit_set(self) -> None:
        """Prompt for new metadata values and update the selected set."""
        selected = self._selected_set()
        if selected is None:
            return
        dialog = SetMetadataDialog(
            self,
            "Edit Set Metadata",
            initial_values={"name": selected.name, "code": selected.code, "date": selected.date, "type": selected.set_type},
        )
        self.wait_window(dialog)
        if not dialog.result:
            return
        try:
            self._content_service.update_set(
                file_path=selected.file_path,
                name=dialog.result["name"],
                code=dialog.result["code"],
                date_value=dialog.result["date"],
                set_type=dialog.result["type"],
            )
        except Exception as exc:
            show_error("Update Failed", str(exc))
            return
        self._on_sets_changed()
        show_info("Set Updated", f"Updated set '{dialog.result['name']}'.")

    def _rename_set(self) -> None:
        """Open the same metadata editor flow, focusing on a set rename operation."""
        self._edit_set()

    def _delete_set(self) -> None:
        """Delete the selected set after confirmation, including unique assets."""
        selected = self._selected_set()
        if selected is None:
            return
        if not confirm_action("Delete Set", f"Delete set '{selected.name}' and its unique assets?"):
            return
        try:
            self._content_service.delete_set(selected)
        except Exception as exc:
            show_error("Delete Failed", str(exc))
            return
        self._on_sets_changed()
        show_info("Set Deleted", f"Deleted set '{selected.name}'.")

    def _export_set(self) -> None:
        """Export the selected set as a .forgepkg.zip archive."""
        selected = self._selected_set()
        if selected is None:
            return
        file_name = filedialog.asksaveasfilename(
            title="Export Forge Package",
            defaultextension=".forgepkg.zip",
            filetypes=[("Forge Package", "*.forgepkg.zip"), ("Zip Archive", "*.zip")],
            initialfile=f"{selected.name}.forgepkg.zip",
        )
        if not file_name:
            return
        try:
            package_path = self._content_service.export_set_package(selected, Path(file_name))
        except Exception as exc:
            show_error("Export Failed", str(exc))
            return
        show_info("Package Exported", f"Exported package to:\n{package_path}")

    def _import_package(self) -> None:
        """Import a previously exported Forge package archive."""
        from forge_content_manager.ui.dialogs import CollisionStrategyDialog

        file_name = filedialog.askopenfilename(
            title="Import Forge Package",
            filetypes=[("Forge Package", "*.forgepkg.zip"), ("Zip Archive", "*.zip")],
        )
        if not file_name:
            return
        collision_dialog = CollisionStrategyDialog(self)
        self.wait_window(collision_dialog)
        if collision_dialog.result is None:
            return
        try:
            summary = self._content_service.import_set_package(Path(file_name), collision_dialog.result)
        except Exception as exc:
            show_error("Import Failed", str(exc))
            return
        self._on_sets_changed()
        detail_lines = [
            f"Set: {summary.imported_set_name} ({summary.imported_set_code})",
            f"Installed cards: {summary.installed_cards}",
            f"Installed images: {summary.installed_images}",
        ]
        if summary.skipped_items:
            detail_lines.append("Skipped items:")
            detail_lines.extend(summary.skipped_items)
        if summary.warnings:
            detail_lines.append("Warnings:")
            detail_lines.extend(summary.warnings)
        show_info("Package Imported", "\n".join(detail_lines))
