"""Card import tab implementation."""

from __future__ import annotations

from collections.abc import Callable

import customtkinter as ctk

from forge_content_manager.services.content_service import ForgeContentService
from forge_content_manager.ui.dialogs import ProgressDialog, show_error, show_info
from forge_content_manager.ui.widgets import CardImportEntryFrame


class CardImportTab(ctk.CTkFrame):
    """Batch import tab for custom card scripts and associated images."""

    def __init__(self, master: ctk.CTkBaseClass, content_service: ForgeContentService, on_import_complete: Callable[[], None]) -> None:
        """Build the batch import layout and initial empty card list."""
        super().__init__(master)
        self._content_service = content_service
        self._on_import_complete = on_import_complete
        self._entry_frames: list[CardImportEntryFrame] = []

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        toolbar = ctk.CTkFrame(self)
        toolbar.grid(row=0, column=0, sticky="ew", padx=16, pady=(16, 8))
        toolbar.grid_columnconfigure(1, weight=1)

        set_label = ctk.CTkLabel(toolbar, text="Destination Set")
        set_label.grid(row=0, column=0, sticky="w", padx=(12, 8), pady=12)

        self.set_menu = ctk.CTkOptionMenu(toolbar, values=["No sets available"])
        self.set_menu.grid(row=0, column=1, sticky="w", padx=8, pady=12)

        add_button = ctk.CTkButton(toolbar, text="Add Card", command=self.add_card_entry, width=120)
        add_button.grid(row=0, column=2, padx=8, pady=12)

        import_button = ctk.CTkButton(toolbar, text="Import All", command=self.import_all, width=120)
        import_button.grid(row=0, column=3, padx=(8, 12), pady=12)

        self.scrollable = ctk.CTkScrollableFrame(self)
        self.scrollable.grid(row=1, column=0, sticky="nsew", padx=16, pady=(0, 16))
        self.scrollable.grid_columnconfigure(0, weight=1)

        self.refresh_sets()
        self.add_card_entry()

    def refresh_sets(self) -> None:
        """Reload the destination set options from the current Forge sets."""
        sets = self._content_service.list_sets()
        if not sets:
            self.set_menu.configure(values=["No sets available"])
            self.set_menu.set("No sets available")
            return
        values = [f"{record.name} [{record.code}]" for record in sets]
        self.set_menu.configure(values=values)
        current_value = self.set_menu.get()
        if current_value not in values:
            self.set_menu.set(values[0])

    def add_card_entry(self) -> None:
        """Append a new card import entry frame to the tab."""
        entry = CardImportEntryFrame(self.scrollable, index=len(self._entry_frames) + 1, on_remove=self.remove_card_entry)
        entry.grid(row=len(self._entry_frames), column=0, sticky="ew", padx=4, pady=8)
        self._entry_frames.append(entry)

    def remove_card_entry(self, entry: CardImportEntryFrame) -> None:
        """Remove a card import entry frame and reflow the remaining list."""
        if len(self._entry_frames) == 1:
            show_error("Cannot Remove", "At least one card entry must remain visible.")
            return
        self._entry_frames.remove(entry)
        entry.destroy()
        for index, frame in enumerate(self._entry_frames, start=1):
            frame.grid_configure(row=index - 1)

    def import_all(self) -> None:
        """Validate the card entry list and import all entries into the selected set."""
        sets = self._content_service.list_sets()
        if not sets:
            show_error("No Sets", "Create a destination set before importing cards.")
            return
        selected_label = self.set_menu.get()
        selected_set = next((record for record in sets if selected_label == f"{record.name} [{record.code}]"), None)
        if selected_set is None:
            show_error("Set Selection", "Select a valid destination set.")
            return
        cards = [entry.get_value() for entry in self._entry_frames]
        if any(not card.script_text.strip() for card in cards):
            show_error("Missing Script", "Each card entry must include Forge script text.")
            return
        progress_dialog = ProgressDialog(self, "Importing Cards")
        try:
            summary = self._content_service.import_cards(
                destination_set=selected_set,
                cards=cards,
                progress_callback=progress_dialog.update_progress,
            )
        except Exception as exc:
            progress_dialog.destroy()
            show_error("Import Failed", str(exc))
            return
        progress_dialog.destroy()
        detail_lines = [
            f"Imported: {summary.imported_count}",
            f"Failed: {summary.failed_count}",
        ]
        for result in summary.results:
            if result.success and result.warnings:
                detail_lines.append(f"{result.card_name}: imported with warnings: {'; '.join(result.warnings)}")
            elif result.success:
                detail_lines.append(f"{result.card_name}: imported")
            else:
                detail_lines.append(f"{result.card_name}: failed: {result.error}")
        show_info("Import Summary", "\n".join(detail_lines))
        if summary.imported_count > 0:
            self._on_import_complete()
