import flet as ft


def main(page: ft.Page):
    page.title = "Calculator App"
    page.update()

    txt_result = ft.TextField(text_align=ft.TextAlign.RIGHT, expand=1, read_only=True)

    def btn_click(e):
        if e.control.text == 'C':
            txt_result.value = ''
        elif e.control.text == '=':
            try:
                txt_result.value = str(eval(txt_result.value))
            except:
                txt_result.value = 'Error'
        else:
            txt_result.value += e.control.text
        page.update()

    buttons = ["789/", "456*", "123-", "0.C+", "="]
    for row in buttons:
        row_controls = []
        for btn_text in row:
            button = ft.TextButton(text=btn_text, on_click=btn_click, expand=1)
            row_controls.append(button)
        page.add(ft.Row(controls=row_controls, expand=1))

    page.add(txt_result)


ft.app(main)
