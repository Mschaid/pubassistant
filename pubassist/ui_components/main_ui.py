from shiny import *

from pubassist.ui_components import SideBar


class MainUI:
    def __init__(self) -> None: ...

    def logo(self):
        img = ui.output_image("render_logo", fill=False)
        return img

    def user_input(self):
        user_input = ui.input_text_area(
            "user_prompt",
            # "test",
            [
                ui.markdown(
                    """        
                        ### Enter your abstract below and I'd be happy to assist:
                """
                ),
                ui.markdown("---"),
            ],
            autoresize="both",
            width="100%",
            height="100%",
            rows=10,
            spellcheck=True,
            placeholder="Enter your abstract here",
        )
        return user_input

    def get_response_button(self):
        button = ui.input_action_button("get_feedback_button", "Get Feedback")
        return button

    def columns(self):
        cols = ui.layout_column_wrap(
            self.user_input(), self.logo(), width=(4 / 1), fixed_width=True
        )
        return cols

    def render(self):
        main_ui = ui.page_fluid(
            self.columns(),
            self.get_response_button(),
        )
        return main_ui
