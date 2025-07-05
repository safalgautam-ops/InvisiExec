from textual.app import App
from textual.widgets import Button, Static, Footer, Header, Input, TextArea
from textual.containers import ScrollableContainer, Vertical, Horizontal, Container
from textual import on
from textual.reactive import reactive
from textual.screen import Screen

class EncodeScreen(Screen):

    def compose(self):
        yield Container(
            Static("Welcome to the Encapsula:Steganography Toolkit", id="title", classes="texts"),
            Static("Encode Your Message Here: ", id="encode_screen", classes="texts"),
            Button("Upload File", variant="primary", id="upload_button"),
            Static("Enter your message here:", id="textbox", classes="texts"),
            TextArea(id="message_input", classes="input-field"),
            Static("Set your password here:", id="passbox", classes="texts"),
            Input(placeholder="Type your password here...", id="password_input", classes="input-field", password=True),
            Page2functional()
        )

    @on(Button.Pressed, "#upload_button")
    def upload_file(self):
        pass

class Page2functional(Static):
    def compose(self):
        yield Horizontal(
            Button("Hide Now", variant="error", id="hiding_button"),
            Button("Go Back", variant="success", id="back_button"),
            id="button-group"
        )

    @on(Button.Pressed, "#encode_button")
    def encode_message(self):
        # Logic to encode the message
        pass

    @on(Button.Pressed, "#back_button")
    def go_back(self):
        self.app.pop_screen()

class DecodeScreen(Screen): 
    def compose(self):
        yield Container(
            Static("Welcome to the Encapsula:Steganography Toolkit", id="title", classes="texts"),
            Static("Decode Your Message Here: ", id="decode_screen", classes="texts"),
            Button("Upload File", variant="primary", id="upload_button"),
            Static("Enter your password here:", id="passbox", classes="texts"),
            Input(placeholder="Type your password here...", id="password_input", classes="input-field", password=True),
            Page3functional()
        )

    @on(Button.Pressed, "#upload_button")
    def upload_file(self):
        pass

class Page3functional(Static):
    def compose(self):
        yield Horizontal(
            Button("Show Now", variant="error", id="showing_button"),
            Button("Go Back", variant="success", id="back_button"),
            id="button-group"
        )

    @on(Button.Pressed, "#showing_button")
    def encode_message(self):
        # Logic to encode the message
        pass

    @on(Button.Pressed, "#back_button")
    def go_back(self):
        self.app.pop_screen()


class Frontdisplay(Static):
    def compose(self):
        yield Vertical(
            Static("Welcome to the Encapsula:Steganography Toolkit", id="title", classes="texts"),
            Static("This tool was designed and developed by", id="subtitle", classes="texts"),
            Static(r"""
 ____  ____    __    ____  ____  _  _  ____ 
(  _ \( ___)  /__\  (  _ \( ___)( \/ )( ___)
 )(_) ))__)  /(__)\  )(_) ))__)  \  /  )__) 
(____/(____)(__)(__)(____/(____) (__) (____)
""", id="ascii", classes="texts"),
            Static("github: safalgautam-ops", id="github", classes="texts"),
            Static("This toolkit allows you to hide messages in images or files.", id="description", classes="texts"),
            Static("Select an option below to get started:", id="instruction", classes="texts"),
            Frontfunctional(),
            id="text-group"
        )

class Frontfunctional(Static):
    def compose(self):
        yield Horizontal(
            Button("Encode", variant="error", id="encode_button"),
            Button("Decode", variant="success", id="decode_button"),
            id="button-group"
        )

    @on(Button.Pressed, "#encode_button")
    def encode_message(self):
        self.app.push_screen(EncodeScreen())

    @on(Button.Pressed, "#decode_button")
    def decode_message(self):
        self.app.push_screen(DecodeScreen())

#ultimately creates a screen object
class Frontpage(App):

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("e", "encode_message", "Encode Message"),
        ("d", "decode_message", "Decode Message")
    ]

    CSS_PATH = "style.css"

    def compose(self):
        yield Header()
        with ScrollableContainer(id="mainUI"):
            yield Container(
                Frontdisplay()
            )
        yield Footer()

def main():
    app = Frontpage()
    app.run()

if __name__ == "__main__":
    main()
