from __future__ import annotations

from typing import TYPE_CHECKING

from je_editor import JEBrowser

if TYPE_CHECKING:
    from test_pioneer.test_pioneer_editor_ui.editor_main.main_ui import AutomationEditor


def open_web_browser(
        automation_editor_instance: AutomationEditor, url: str, tab_name: str) -> None:
    automation_editor_instance.tab_widget.addTab(
        JEBrowser(start_url=url),
        f"{tab_name}{automation_editor_instance.tab_widget.count()}"
    )
