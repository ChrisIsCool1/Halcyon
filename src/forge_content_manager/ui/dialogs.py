"""Reusable dialog windows used across the Forge content manager UI."""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox

import customtkinter as ctk


def show_error(title: str, message: str) -> None:
    """Display an error dialog to the user."""
    messagebox.showerror(title, message)


def show_info(title: str, message: str) -> None:
    """Display an informational dialog to the user."""
    messagebox.showinfo(title, message)


def confirm_action(title: str, message: str) -> bool:
    """Prompt the user to confirm a potentially destructive action."""
    return messagebox.askyesno(title, message)


class SetMetadataDialog(ctk.CTkToplevel):
    """Modal dialog used to create or edit Forge set metadata."""

    def __init__(
        self,
        master: tk.Misc,
        title: str,
        initial_values: dict[str, str] | None = None,
    ) -> None:
        """Build the dialog inputs and wait for the user to confirm or cancel."""
        super().__init__(master)
        self.title(title)
        self.geometry("420x300")
        self.resizable(False, False)
        self.transient(master)
        self.grab_set()
        self.result: dict[str, str] | None = None

        values = initial_values or {}
        self.grid_columnconfigure(1, weight=1)

        labels = [
            ("Set Name", "name", values.get("name", "")),
            ("Set Code", "code", values.get("code", "")),
            ("Date", "date", values.get("date", "")),
            ("Type", "type", values.get("type", "Custom")),
        ]
        self._entries: dict[str, ctk.CTkEntry] = {}
        for row, (label_text, key, value) in enumerate(labels):
            label = ctk.CTkLabel(self, text=label_text)
            label.grid(row=row, column=0, sticky="w", padx=18, pady=(16 if row == 0 else 8, 8))
            entry = ctk.CTkEntry(self)
            entry.insert(0, value)
            entry.grid(row=row, column=1, sticky="ew", padx=18, pady=(16 if row == 0 else 8, 8))
            self._entries[key] = entry

        button_bar = ctk.CTkFrame(self, fg_color="transparent")
        button_bar.grid(row=len(labels), column=0, columnspan=2, sticky="e", padx=18, pady=18)

        cancel_button = ctk.CTkButton(button_bar, text="Cancel", command=self.destroy, width=100)
        cancel_button.pack(side="right", padx=(10, 0))

        save_button = ctk.CTkButton(button_bar, text="Save", command=self._submit, width=100)
        save_button.pack(side="right")

        self.protocol("WM_DELETE_WINDOW", self.destroy)
        self.wait_visibility()
        self.focus()

    def _submit(self) -> None:
        """Persist the entered values into the dialog result and close the window."""
        self.result = {key: entry.get().strip() for key, entry in self._entries.items()}
        self.destroy()


class CollisionStrategyDialog(ctk.CTkToplevel):
    """Modal dialog for choosing package import collision behavior."""

    def __init__(self, master: tk.Misc) -> None:
        """Build a compact collision strategy chooser."""
        super().__init__(master)
        self.title("Package Collision Handling")
        self.geometry("420x240")
        self.resizable(False, False)
        self.transient(master)
        self.grab_set()
        self.result: str | None = None

        description = ctk.CTkLabel(
            self,
            text="Choose how to handle existing files while importing a Forge package.",
            justify="left",
            wraplength=360,
        )
        description.pack(fill="x", padx=18, pady=(18, 12))

        self._value = tk.StringVar(value="skip")
        for label, value in (("Skip existing files", "skip"), ("Replace existing files", "replace"), ("Rename imported files", "rename")):
            radio = ctk.CTkRadioButton(self, text=label, value=value, variable=self._value)
            radio.pack(anchor="w", padx=18, pady=6)

        button_bar = ctk.CTkFrame(self, fg_color="transparent")
        button_bar.pack(fill="x", padx=18, pady=18)
        button_bar.grid_columnconfigure(0, weight=1)

        cancel_button = ctk.CTkButton(button_bar, text="Cancel", command=self.destroy, width=100)
        cancel_button.pack(side="right", padx=(10, 0))

        import_button = ctk.CTkButton(button_bar, text="Import", command=self._submit, width=100)
        import_button.pack(side="right")

    def _submit(self) -> None:
        """Store the selected strategy and close the dialog."""
        self.result = self._value.get()
        self.destroy()


class CardsFolderHelpDialog(ctk.CTkToplevel):
    """Explain how to obtain and configure Forge's reference cardsfolder."""

    def __init__(self, master: tk.Misc) -> None:
        """Build a modal, readable walkthrough for the cardsfolder workflow."""
        super().__init__(master)
        self.title("How to import a Forge cardsfolder")
        self.geometry("680x610")
        self.minsize(560, 500)
        self.transient(master)
        self.grab_set()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(
            self,
            text="Add Forge's card scripts to the Script Editor",
            font=ctk.CTkFont(size=22, weight="bold"),
            anchor="w",
        ).grid(row=0, column=0, sticky="ew", padx=24, pady=(22, 8))

        instructions = ctk.CTkTextbox(self, wrap="word", activate_scrollbars=True)
        instructions.grid(row=1, column=0, sticky="nsew", padx=24, pady=(0, 16))
        instructions.insert(
            "1.0",
            "This optional library lets the Script Editor search the card scripts that ship with Forge. "
            "It does not change your installed Forge cards.\n\n"
            "1. Find Forge's card archive\n"
            "Open the folder where you extracted a Forge release. Inside it, look for:\n\n"
            "    res\\cardsfolder\\cardsfolder.zip\n\n"
            "This is the Forge release's ZIP, not the Halcyon release ZIP. The `res` folder may be beside "
            "the Forge launcher or application files.\n\n"
            "2. Copy the ZIP somewhere convenient\n"
            "Copy `cardsfolder.zip` to a location you can keep, such as a folder under Documents. "
            "Do not remove it out of the Forge release, as this may cause errors with your Forge installation.\n\n"
            "3. Choose how to import it\n"
            "In Settings, under Script Editor Reference Cards, click \"Choose cardsfolder\". Select \"Zipped "
            "cardsfolder\" to choose the ZIP, or \"Unzipped folder\" to choose a folder that has already been "
            "extracted. Halcyon extracts a selected ZIP into its own managed folder and leaves the archive "
            "unchanged. Card scripts may be nested in letter-named folders inside the archive.\n\n"
            "4. Wait for indexing\n"
            "Halcyon builds a searchable index in the background. When it finishes, open Script Editor and "
            "use Reference Cards to search the Forge card scripts. Large releases can take a little while.\n\n"
            "If it does not find any cards\n"
            "Check that the selected folder or ZIP contains `.txt` card scripts. You can return here and "
            "choose a different source at any time.",
        )
        instructions.configure(state="disabled")

        ctk.CTkButton(self, text="Close", command=self.destroy, width=110).grid(
            row=2, column=0, sticky="e", padx=24, pady=(0, 22)
        )
        self.protocol("WM_DELETE_WINDOW", self.destroy)
        self.wait_visibility()
        self.focus()


class CardsFolderImportDialog(ctk.CTkToplevel):
    """Let the user choose an extracted cardsfolder or a ZIP archive."""

    def __init__(self, master: tk.Misc) -> None:
        """Build a modal chooser and store the selected source format."""
        super().__init__(master)
        self.title("Choose cardsfolder format")
        self.geometry("420x220")
        self.resizable(False, False)
        self.transient(master)
        self.grab_set()
        self.result: str | None = None

        ctk.CTkLabel(
            self,
            text="How would you like to import the Forge cardsfolder?",
            justify="left",
            wraplength=370,
        ).pack(fill="x", padx=20, pady=(24, 18))

        buttons = ctk.CTkFrame(self, fg_color="transparent")
        buttons.pack(fill="x", padx=20, pady=(0, 20))
        ctk.CTkButton(
            buttons,
            text="Unzipped folder",
            command=lambda: self._submit("folder"),
        ).pack(fill="x", pady=(0, 10))
        ctk.CTkButton(
            buttons,
            text="Zipped cardsfolder (.zip)",
            command=lambda: self._submit("zip"),
        ).pack(fill="x")

        self.protocol("WM_DELETE_WINDOW", self.destroy)
        self.wait_visibility()
        self.focus()

    def _submit(self, source_type: str) -> None:
        """Store the chosen source format and close the modal."""
        self.result = source_type
        self.destroy()


class ProgressDialog(ctk.CTkToplevel):
    """Progress dialog for longer-running import operations."""

    def __init__(self, master: tk.Misc, title: str) -> None:
        """Build the dialog shell and initial progress widgets."""
        super().__init__(master)
        self.title(title)
        self.geometry("420x180")
        self.resizable(False, False)
        self.transient(master)
        self.grab_set()

        self._label = ctk.CTkLabel(self, text="Preparing...", wraplength=360)
        self._label.pack(fill="x", padx=18, pady=(24, 12))

        self._progress = ctk.CTkProgressBar(self)
        self._progress.set(0)
        self._progress.pack(fill="x", padx=18, pady=12)

        self._counter = ctk.CTkLabel(self, text="0 / 0")
        self._counter.pack(fill="x", padx=18, pady=(4, 18))

        self.update_idletasks()

    def update_progress(self, current: int, total: int, message: str) -> None:
        """Update the progress display using the latest operation state."""
        self._label.configure(text=message)
        progress_value = 0 if total == 0 else min(max(current / total, 0), 1)
        self._progress.set(progress_value)
        self._counter.configure(text=f"{current} / {total}")
        self.update_idletasks()
