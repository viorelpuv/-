from tkinter import *
from tkinter.ttk import Notebook

root = Tk()
root.config(bg='white')
root.geometry("900x650")
root.title("Шестерочка")
root.resizable(False, False)

notebook = Notebook(root)

page1 = Frame(notebook, width=650, height=550, bg='white')
page2 = Frame(notebook, width=650, height=550, bg='white')
page3 = Frame(notebook, width=650, height=550, bg='white')
page4 = Frame(notebook, width=650, height=550, bg='white')
page5 = Frame(notebook, width=650, height=550, bg='white')

notebook.add(page1, text=f'{"Выпечка": ^33}')
notebook.add(page2, text=f'{"Горячее": ^33}')
notebook.add(page3, text=f'{"Салаты": ^33}')
notebook.add(page4, text=f'{"Десерты": ^33}')
notebook.add(page5, text=f'{"Напитки": ^33}')

notebook.place(x=130, y=50)


def hover(widget, on_entrance, on_exit, entrance_fg, exit_fg):
    widget.bind("<Enter>", func=lambda e: widget.config(
        bg=on_entrance, fg=entrance_fg))
    widget.bind("<Leave>", func=lambda e: widget.config(
        bg=on_exit, fg=exit_fg))


def signup():
    signup_window = Tk()
    signup_window.title("Регистрация")
    signup_window.geometry("600x300")
    signup_window.resizable(False, False)

    user_name_var = StringVar()
    password_var = StringVar()
    name_var = StringVar()

    signup_canvas = Canvas(signup_window, width=720, height=440, bg="white")
    signup_canvas.pack()

    signup_frame = Frame(signup_canvas, bg="white", highlightbackground='black', highlightthickness=4)
    signup_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    title = Label(signup_frame, text="Signup to Continue", fg="black", bg="white")
    title.config(font=('calibri', 25))
    title.place(x=120, y=25)

    from tkinter import *


from tkinter.ttk import Notebook
from tkinter import scrolledtext
from tkinter import messagebox
import webbrowser
import datetime

line = '_______________________________________________________________________________________________________________'

root = Tk()
root.config(bg='white')
root.geometry("900x650")
root.title("Шестерочка")
root.resizable(False, False)

notebook = Notebook(root)

page1 = Frame(notebook, width=650, height=550, bg='white')
page2 = Frame(notebook, width=650, height=550, bg='white')
page3 = Frame(notebook, width=650, height=550, bg='white')
page4 = Frame(notebook, width=650, height=550, bg='white')
page5 = Frame(notebook, width=650, height=550, bg='white')

notebook.add(page1, text=f'{"Выпечка": ^33}')
notebook.add(page2, text=f'{"Горячее": ^33}')
notebook.add(page3, text=f'{"Салаты": ^33}')
notebook.add(page4, text=f'{"Десерты": ^33}')
notebook.add(page5, text=f'{"Напитки": ^33}')

notebook.place(x=130, y=50)


def hover(widget, on_entrance, on_exit, entrance_fg, exit_fg):
    widget.bind("<Enter>", func=lambda e: widget.config(
        bg=on_entrance, fg=entrance_fg))
    widget.bind("<Leave>", func=lambda e: widget.config(
        bg=on_exit, fg=exit_fg))


def signup():
    signup_window = Tk()
    signup_window.title("Регистрация")
    signup_window.geometry("600x300")
    signup_window.resizable(False, False)

    user_name_var = StringVar()
    password_var = StringVar()
    name_var = StringVar()

    signup_canvas = Canvas(signup_window, width=720, height=440, bg="white")
    signup_canvas.pack()

    signup_frame = Frame(signup_canvas, bg="white", highlightbackground='black', highlightthickness=4)
    signup_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    title = Label(signup_frame, text="Регистрация", fg="black", bg="white")
    title.config(font=('calibri', 25))
    title.place(x=120, y=25)

    username_entry = Entry(signup_frame, highlightbackground='black', highlightthickness=4, textvariable=user_name_var)
    username_label = Label(signup_frame, text='Логин: ', bg='white', fg='black')
    username_entry.place(x=200, y=80)
    username_label.place(x=100, y=80)

    password_entry = Entry(signup_frame, highlightbackground='black', highlightthickness=4, textvariable=password_var,
                           show='•')
    password_label = Label(signup_frame, text='Пароль: ', bg='white', fg='black')
    password_entry.place(x=200, y=120)
    password_label.place(x=100, y=120)

    name_entry = Entry(signup_frame, highlightbackground='black', highlightthickness=4, textvariable=name_var)
    name_label = Label(signup_frame, text='Имя ', bg='white', fg='black')
    name_entry.place(x=200, y=160)
    name_label.place(x=100, y=160)

    def exit_signup():
        name = name_entry.get()
        global root_name_label
        root_name_label = Label(root, text=f'Аккаунт: {name}', bg='white', fg='black',
                                font=('Calibri', 14, 'bold'))
        root_name_label.place(x=600, y=10)
        signup_window.destroy()

    name_entry.bind("<Return>", exit_signup)

    signup_button = Button(signup_frame, text='Вход', command=exit_signup, fg="white", bg="black",
                           relief=FLAT, width=15, height=1)
    signup_button.configure(activebackground="#33B5E5")
    hover(signup_button, on_entrance='#0E76A9', on_exit='black', entrance_fg='white', exit_fg='white')
    signup_button.place(x=180, y=200)

    signup_window.mainloop()


def tb():
    cart = Tk()
    cart.geometry("800x550")
    cart.title("Корзина")
    cart.config(bg='white')

    items = scrolledtext.ScrolledText(cart, font=('times', 12), bg='white', fg='black')
    items.place(x=1, y=40)

    burger_p = 3.55
    burger_quantity = burger_Q.get()

    fries_p = 4.70
    fries_quantity = fries_Q.get()

    wings_p = 8
    wings_quantity = wings_Q.get()

    sticks_p = 2.75
    sticks_quantity = sticks_Q.get()

    fingers_p = 4.55
    fingers_quantity = fingers_Q.get()

    rice_p = 8.45
    rice_quantity = rice_Q.get()

    chops_p = 8.75
    chops_quantity = chops_Q.get()

    meatloaf_p = 7.60
    meatloaf_quantity = meatloaf_Q.get()

    salmon_p = 6.50
    salmon_quantity = salmon_Q.get()

    tuna_p = 8.90
    tuna_quantity = tuna_Q.get()

    mushroom_p = 7.50
    mushroom_quantity = mushroom_Q.get()

    cauliflower_p = 7.30
    cauliflower_quantity = cauliflower_Q.get()

    macaroni_p = 6.00
    macaroni_quantity = macaroni_Q.get()

    noodles_p = 7.75
    noodles_quantity = noodles_Q.get()

    sandwich_p = 3.50
    sandwich_quantity = sandwich_Q.get()

    cake_p = 10.00
    cake_quantity = cake_Q.get()

    apple_p = 5.00
    apple_quantity = apple_Q.get()

    split_p = 8.25
    split_quantity = split_Q.get()

    cream_pie_p = 6.10
    cream_pie_quantity = cream_pie_Q.get()

    pudding_p = 5.55
    pudding_quantity = pudding_Q.get()

    cold_p = 3.50
    cold_quantity = cold_Q.get()

    strawberry_p = 3.00
    strawberry_quantity = strawberry_Q.get()

    watermelon_p = 2.70
    watermelon_quantity = watermelon_Q.get()

    tea_p = 2.00
    tea_quantity = tea_Q.get()

    coffee_p = 2.00
    coffee_quantity = coffee_Q.get()

    if burger_Var != '0':
        items.insert("1.0", f"Запеченная картошка: ${burger_p * int(burger_quantity)}; Количество: {burger_quantity}")

    if fries_var != 0:
        items.insert("2.0", f"\nСухарики 3 корочки: ${fries_p * int(fries_quantity)}; Количество: {fries_quantity}")

    if wings_var != 0:
        items.insert("3.0", f"\nВедро чеснока: ${wings_p * int(wings_quantity)}; Количество: {wings_quantity}")

    if sticks_var != 0:
        items.insert("4.0", f"\nТараканы в кляре: ${sticks_p * int(sticks_quantity)}; Количество: {sticks_quantity}")

    if fingers_var != 0:
        items.insert("5.0", f"\nБагет: ${fingers_p * int(fingers_quantity)}; Количество: {fingers_quantity}")

    if rice_Var != 0:
        items.insert("7.0", f"\n \nГороховый суп: ${rice_p * int(rice_quantity)}; Количество: {rice_quantity}")

    if chops_var != 0:
        items.insert("8.0",
                     f"\nКотлета из отчисленного: ${chops_p * int(chops_quantity)}; Количество: {chops_quantity}")

    if meatloaf_var != 0:
        items.insert("9.0",
                     f"\nСосиски из индусов: ${meatloaf_p * int(meatloaf_quantity)}; Количество: {meatloaf_quantity}")

    if salmon_var != 0:
        items.insert("10.0", f"\nОбед первокурсника: ${salmon_p * int(salmon_quantity)}; Количество: {salmon_quantity}")

    if tuna_var != 0:
        items.insert("11.0", f"\nГолубцы из голубей: ${tuna_p * int(tuna_quantity)}; Количество: {tuna_quantity}")

    if mushroom_Var != 0:
        items.insert("12.0",
                     f'\nСалат студенческий: ${mushroom_p * int(mushroom_quantity)}; Количество: {mushroom_quantity}')

    if cauliflower_var != 0:
        items.insert("13.0",
                     f"\nСалат студенческий для платников: ${cauliflower_p * int(cauliflower_quantity)}; Количество:"
                     f" {cauliflower_quantity}")

    if macaroni_var != 0:
        items.insert("14.0",
                     f"\nСалат ультра люкс плюс: ${macaroni_p * int(macaroni_quantity)}; Количество: {macaroni_quantity}")

    if noodles_var != 0:
        items.insert("15.0", f"\nВилка: ${noodles_p * int(noodles_quantity)}; Количество: {noodles_quantity}")

    if sandwich_var != 0:
        items.insert("16.0",
                     f"\nЦена к салату: ${sandwich_p * int(sandwich_quantity)}; Количество: {sandwich_quantity}")

    if cake_Var != 0:
        items.insert("17.0", f"\nМуха в шоколаде: ${cake_p * int(cake_quantity)}; Количество: {cake_quantity}")

    if apple_var != 0:
        items.insert("18.0",
                     f"\nСеледка в шубе из ЦУМа: ${apple_p * int(apple_quantity)}; Количество: {apple_quantity}")

    if split_var != 0:
        items.insert("19.0", f"\nБанан: ${split_p * int(split_quantity)}; Количество: {apple_quantity}")

    if cream_pie_var != 0:
        items.insert("20.0", f"\nЛожка: ${cream_pie_p * int(cream_pie_quantity)}; Количество: {cream_pie_quantity}")

    if pudding_var != 0:
        items.insert("21.0",
                     f"\nПодсолнечное масло: ${pudding_p * int(pudding_quantity)}; Количество: {pudding_quantity}")

    if cold_Var != 0:
        items.insert("22.0", f"\nКвас: ${cold_p * int(cold_p)}; Количество: {cold_quantity}")

    if strawberry_var != 0:
        items.insert("23.0",
                     f"\nСлезы четверокурсников: ${strawberry_p * int(strawberry_quantity)}; Количество: "
                     f"{strawberry_quantity}")

    if watermelon_var != 0:
        items.insert("24.0",
                     f"\nМои слезы: ${watermelon_p * int(watermelon_quantity)}; Количество:"
                     f" {watermelon_quantity}")

    if tea_var != 0:
        items.insert("25.0", f"\nСтакан: ${tea_p * int(tea_quantity)}; Количество: {tea_quantity}")

    if coffee_var != 0:
        items.insert("26.0", f"\nСлабительное: ${coffee_p * int(coffee_quantity)}; Количество: {coffee_quantity}")

    total = (float(burger_p) * float(burger_quantity)) + (float(fries_p) * float(fries_quantity)) + \
            (float(wings_p) * float(wings_quantity)) + (float(meatloaf_p) * float(meatloaf_quantity)) + \
            (float(sticks_p) * float(sticks_quantity)) + (float(fingers_p) * float(fingers_quantity)) + \
            (float(rice_p) * float(rice_quantity)) + (float(chops_p) * float(chops_quantity)) + \
            (float(meatloaf_p) * float(meatloaf_quantity)) + (float(salmon_p) * float(salmon_quantity)) + \
            (float(tuna_p) * float(tuna_quantity)) + (float(mushroom_p) * float(mushroom_quantity)) + \
            (float(cauliflower_p) * float(cauliflower_quantity)) + (float(macaroni_p) * float(macaroni_quantity)) + \
            (float(noodles_p) * float(noodles_quantity)) + (float(sandwich_p) * float(sandwich_quantity)) + \
            (float(apple_p) * float(apple_quantity)) + (float(cake_p) * float(cake_quantity)) + \
            (float(split_p) * float(split_quantity)) + (float(cream_pie_p) * float(cream_pie_quantity)) + \
            (float(pudding_p) * float(pudding_quantity)) + (float(cold_p) * float(cold_quantity)) + \
            (float(strawberry_p) * float(strawberry_quantity)) + (float(watermelon_p) * float(watermelon_quantity)) + \
            (float(tea_p) * float(tea_quantity)) + (float(coffee_p) * float(coffee_quantity))

    print(total)

    total_label = Label(cart, text=f"Всего:  ${total}", bg='white', fg='black', font=('Calibri', 14, 'bold'))
    total_label.place(x=685, y=50)

    def details():
        global details_top_level
        details_top_level = Toplevel()
        details_top_level.geometry("500x250")
        details_top_level.title("Покупка")
        details_top_level.resizable(False, False)
        details_top_level.configure(bg='white')

        details_frame = Frame(details_top_level, bg="white", highlightbackground='black', highlightthickness=4)
        details_frame.place(relx=0.5, rely=0.1, relwidth=0.85, relheight=0.85, anchor='n')

        shipping_address_label = Label(details_frame, text='Адрес доставки', bg='white', fg='black',
                                       font=("Calibri", 10, 'bold'))
        shipping_address_label.place(x=25, y=20)

        shipping_address_entry = Entry(details_frame, width=15, highlightbackground='black',
                                       highlightthickness=4)
        shipping_address_entry.place(x=250, y=20)

        billing_address_label = Label(details_frame, text='Номер квартиры', bg='white', fg='black',
                                      font=("Calibri", 10, 'bold'))
        billing_address_label.place(x=25, y=100)

        billing_address_entry = Entry(details_frame, width=15, highlightbackground='black',
                                      highlightthickness=4)
        billing_address_entry.place(x=250, y=100)

        total_label1 = Label(details_frame, text=f"Всего: ${total}", bg='white', fg='black',
                             font=('Calibri', 12, 'bold'))
        total_label1.place(x=25, y=150)

        checkout_button = Button(details_frame, text='Дальше', bg='black', fg='white', command=checkout,
                                 relief=FLAT)

        hover(checkout_button, on_entrance='#0E76A9', on_exit='black', entrance_fg='white', exit_fg='white')
        checkout_button.place(x=250, y=170)

    def checkout():
        # cart.destroy()

        details_top_level.destroy()
        checkout_top_level = Toplevel()
        checkout_top_level.geometry("600x350")
        checkout_top_level.resizable(False, False)
        checkout_top_level.configure(bg='white')
        checkout_top_level.title("Оплата")

        checkout_frame = Frame(checkout_top_level, bg="white", highlightbackground='black', highlightthickness=4)
        checkout_frame.place(relx=0.5, rely=0.1, relwidth=0.85, relheight=0.85, anchor='n')

        card_label = Label(checkout_frame, bg='white', fg='black', text='Карта/кредитка',
                           font=('Calibri', 12, 'bold'))
        card_label.place(x=50, y=100)

        card_name_label = Label(checkout_frame, text='Номер карты', bg='white', fg='black', font=('Calibri', 12))
        card_name_label.place(x=300, y=100)
        card_name_entry = Entry(checkout_frame, highlightbackground='black', highlightthickness=4)
        card_name_entry.place(x=400, y=100)

        card_no_label = Label(checkout_frame, text='Годна до', bg='white', fg='black', font=('Calibri', 12))
        card_no_label.place(x=50, y=140)
        card_no_entry = Entry(checkout_frame, highlightbackground='black', highlightthickness=4)
        card_no_entry.place(x=150, y=140)

        card_expiry_label = Label(checkout_frame, text='CVV\CVC', bg='white', fg='black', font=('Calibri', 12))
        card_expiry_label.place(x=300, y=140)
        card_expiry_entry = Entry(checkout_frame, highlightbackground='black', highlightthickness=4)
        card_expiry_entry.place(x=400, y=140)

        def summary():
            summary_top_level = Toplevel()
            summary_top_level.geometry("400x250")
            summary_top_level.resizable(False, False)
            summary_top_level.title("Summary")

        def verify_card():
            global year
            global month
            card_no = card_no_entry.get()

            card_date = card_expiry_entry.get()

            try:

                month, year = card_date.split('/')

            except ValueError:
                messagebox.showerror(
                    "Ошибка",
                    "Введите дату в формате: 'mm/yyyy' "
                )

            is_valid_date = True
            try:
                datetime.datetime(int(year), int(month), day=1)
            except ValueError:
                is_valid_date = False

            if len(card_no) != 19:
                messagebox.showerror("Ошибка",
                                     """Вы ввели неправильный номер карты""",
                                     icon='error')

            card_name = card_name_entry.get()
            if is_valid_date is True and len(card_no) == 19:
                messagebox.showinfo(
                    "Успешно!",
                    f"${total} были успешно оплачены с карты {card_name}",
                    icon='info'
                )

            else:
                messagebox.showerror(
                    "Ошибка",
                    "Эта карта ошибка"
                )

        card_button = Button(checkout_frame, text='Продолжить', bg='black', fg='white', relief=FLAT,
                             font=('Calibri', 9), command=verify_card)
        hover(card_button, on_entrance='#0E76A9', on_exit='black', entrance_fg='white', exit_fg='white')
        card_button.place(x=540, y=140)

        cash_label = Label(checkout_frame, text='Оплата при получении', font=('Calibri', 12, 'bold'), fg='black',
                           bg='white')
        cash_label.place(x=50, y=210)

        def cash_on_delivery():
            cash_toplevel = Toplevel()
            cash_toplevel.title("При получении")
            cash_toplevel.geometry("600x300")
            cash_toplevel.config(bg='white')
            cash_toplevel.resizable(False, False)

            price_label1 = Label(cash_toplevel, text=f'Всего: ${total}', bg='white', fg='black',
                                 font=('Calibri', 12, 'bold'))
            price_label1.place(x=35, y=50)

            title_label = Label(cash_toplevel, text='Оплата при получении', bg='white', fg='black',
                                font=('Calibri', 15, 'bold'))
            title_label.place(x=200, y=25)

            instructions_label = Label(cash_toplevel, text=f"""
            Оплата будет производиться никогда, т.к. у меня нет ИП и это незаконно. 

            ...А еще я пока не придумал как сделать оплату """,
                                       fg='black', bg='white', font=("Calibri", 12))

            instructions_label.place(x=0, y=150)

        cash_checkbutton = Checkbutton(checkout_frame, text='При получении', onvalue=1, offvalue=0,
                                       bg='white', command=cash_on_delivery,
                                       fg='black', font=('Calibri', 12))
        cash_checkbutton.place(x=200, y=210)

        checkout_top_level.geometry("800x500")
        net_label = Label(checkout_frame, bg='white', fg='black', text='Оплатить онлайн',
                          font=('Calibri', 12, 'bold'))
        net_label.place(x=50, y=50)

        def net_banks():
            net_top_level = Toplevel()
            net_top_level.configure(bg='white')
            net_top_level.resizable(False, False)
            net_top_level.geometry("350x150")
            net_top_level.title("Оплата онлайн ")

            def bank1_command():
                webbrowser.open("https://online.sberbank.ru/CSAFront/index.do")
                net_top_level.destroy()

            def bank2_command():
                webbrowser.open("https://www.tinkoff.ru/")
                net_top_level.destroy()

            def bank3_command():
                webbrowser.open(
                    "https://alfabank.ru/get-money/credit-cards/land/100-days-cpc/?platformId=Yandex_cpc_Y-100days-ac-brand-key-tgo-search-web-delivery-tcpa-66588182_37698840653_desktop_41_search&utm_source=yandex&utm_medium=cpc&utm_campaign=Y_100days_ac_brand_key_tgo_search_web_delivery_tcpa%7C66588182&utm_term=альфа%20банк&utm_content=campaign_type_type1%7Ccampaign_id_66588182%7Cgbid_4723345415%7Cad_id_11516623081%7Cphrase_id_37698840653%7Cretargeting_id_37698840653%7Ccoef_goal_context_id_0%7Cmatch_type_%7Cmatched_keyword_%7Cadtarget_id_37698840653%7Cadtarget_name_%7Cposition_type_premium%7Cposition_1%7Csource_type_search%7Csource_none%7Cdevice_type_desktop%7Cregion_name_Йошкар-Ола%7Cregion_id_41&k50id=0100000037698840653_37698840653&yclid=7400153745715888127")
                net_top_level.destroy()

            def bank4_command():
                webbrowser.open("https://www.open.ru/")
                net_top_level.destroy()

            banks_label = Label(net_top_level, text='Выберите банк: ', bg='white', fg='black',
                                font=("Calibri", 12, 'bold'))
            banks_label.place(x=25, y=1)

            bank1_checkbutton = Checkbutton(net_top_level, text='Сбербанк', bg='white', fg='black',
                                            command=bank1_command)
            bank1_checkbutton.place(x=25, y=25)

            bank2_checkbutton = Checkbutton(net_top_level, text='Тинькофф', bg='white', fg='black',
                                            command=bank2_command)
            bank2_checkbutton.place(x=25, y=50)

            bank3_checkbutton = Checkbutton(net_top_level, text='Альфа банк', bg='white', fg='black',
                                            command=bank3_command)
            bank3_checkbutton.place(x=25, y=75)

            bank4_checkbutton = Checkbutton(net_top_level, text='Банк открытие', bg='white', fg='black',
                                            command=bank4_command)
            bank4_checkbutton.place(x=25, y=100)

        net_button = Button(checkout_frame, text='Выбрать банк', bg='black', fg='white', command=net_banks)
        hover(net_button, on_entrance='#0E76A9', on_exit='black', entrance_fg='white', exit_fg='white')
        net_button.place(x=350, y=50)

    details_button = Button(cart, text='Заказать', bg='#0E76A9', fg='white', relief=FLAT, font="Calibri",
                            width=10, command=details)
    details_button.place(x=700, y=230)
    hover(details_button, on_entrance='black', on_exit='#0E76A9', exit_fg='white', entrance_fg='white')


def sign_out():
    messagebox.showwarning(
        "Выход",
        "Вы уверены, что хотите выйти?",
        icon='question',
    )
    root_name_label.destroy()
    signup()


def signup_box():
    signup_messagebox = messagebox.askyesno(
        "Регистрация",
        "Хотите ли вы зарегистрироваться?",
        icon='question'
    )

    if signup_messagebox:
        signup()


def quit_app():
    quit_messagebox = messagebox.askokcancel(
        "Выход",
        "Вы точно хотите выйти?",
        icon='warning'
    )

    if quit_messagebox:
        root.quit()


def about():
    messagebox.showinfo(
        "О нас",
        """
        Наше кафе - проект, сделанный на коленке, в 12 часов ночи для защиты проекта. Считаем, это заслуживает 5
        """
    )


burger_label = Label(page1, text='Запеченая картошка', bg='white', font=("Calibri", 18), fg='#0E76A9')
burger_label.place(x=250, y=1)

burger_description = Label(page1, text="Запеченная бульба с нежной корочкой в угле",
                           bg='white', fg='#0E76A9', font=('Calibri', 13))
burger_description.place(x=100, y=35)

burger_price = Label(page1, text=' $3.55', font=('Calibri', 15, "bold"), bg='white', fg='#0E76A9')
burger_price.place(x=520, y=80)

burger_cart_button = Button(page1, text='В корзину', font='Calibri', bg='#0E76A9', fg='white', relief=FLAT,
                            command=tb)
burger_cart_button.place(x=25, y=80)
hover(burger_cart_button, on_entrance='black', entrance_fg='white', on_exit='#0E76A9', exit_fg='white')

burger_Var = IntVar()
burger_Var.set("0")
burger_Q = Entry(page1, highlightbackground='#0E76A9', highlightthickness=4, textvariable=burger_Var)
burger_Q.place(x=250, y=80)
burger_Q_label = Label(page1, text='Кол-во: ', bg='white', fg='#0E76A9', font=('Calibri', 12))
burger_Q_label.place(x=180, y=80)

Label(page1, text=line + '_________________', bg='white').place(x=1, y=120)

fries_label = Label(page1, text='Сухарики 3 корочки', bg='white', font=("Calibri", 18), fg='black')
fries_label.place(x=250, y=140)

fries_description = Label(page1, text=
"""Остатки из пачки сухариков 3 корочки""",
                          bg='white', fg='black', font=('Calibri', 13))
fries_description.place(x=100, y=175)

fries_price = Label(page1, text=' $4.65', font=('Calibri', 15, "bold"), bg='white', fg='black')
fries_price.place(x=520, y=220)

fries_cart_button = Button(page1, text='В корзину', font='Calibri', bg='black', fg='white', relief=FLAT, command=tb)
fries_cart_button.place(x=25, y=220)
hover(fries_cart_button, on_entrance='#0E76A9', entrance_fg='white', on_exit='black', exit_fg='white')

fries_var = IntVar()
fries_var.set(0)
fries_Q = Entry(page1, highlightbackground='black', highlightthickness=4, textvariable=fries_var)
fries_Q.place(x=250, y=220)
fries_Q_label = Label(page1, text='Кол-во: ', bg='white', fg='black', font=('Calibri', 12))
fries_Q_label.place(x=180, y=220)

Label(page1, text=line + '_________________', bg='white').place(x=1, y=260)

wings_label = Label(page1, text='Ведро чеснока', bg='white', font=("Calibri", 18), fg='#0E76A9')
wings_label.place(x=250, y=285)

wings_description = Label(page1, text=
"""Ведро с рисунком чеснока, аппетитно и необычно""",
                          bg='white', fg='#0E76A9', font=('Calibri', 13))
wings_description.place(x=100, y=320)

wings_price = Label(page1, text=' $8.00', font=('Calibri', 15, "bold"), bg='white', fg='#0E76A9')
wings_price.place(x=520, y=370)

wings_cart_button = Button(page1, text='В корзину', font='Calibri', bg='#0E76A9', fg='white', relief=FLAT,
                           command=tb)
wings_cart_button.place(x=25, y=370)
hover(wings_cart_button, on_entrance='black', entrance_fg='white', on_exit='#0E76A9', exit_fg='white')

wings_var = IntVar()
wings_var.set(0)
wings_Q = Entry(page1, highlightbackground="#0E76A9", highlightthickness=4, textvariable=wings_var)
wings_Q.place(x=250, y=370)
wings_Q_label = Label(page1, text='Кол-во: ', bg='white', fg='#0E76A9', font=('Calibri', 12))
wings_Q_label.place(x=180, y=370)

Label(page1, text=line + '_________________', bg='white', fg='black').place(x=1, y=400)

Label(page1, text='Другое', bg='white', fg='black', font=("Calibri", 15, "bold")).place(x=250, y=430)

sticks_label = Label(page1, text="Тараканы в кляре", fg='black', bg='white', font=('Calibri', 13, "bold"))
sticks_label.place(x=25, y=470)
sticks_cart_button = Button(page1, text='$2.75', relief=FLAT,
                            command=tb, bg='black', fg='white', font='Calibri')
sticks_cart_button.place(x=450, y=465)

sticks_var = IntVar()

sticks_Q = Entry(page1, highlightbackground='black', highlightthickness=4, textvariable=sticks_var)
sticks_Q.place(x=250, y=470)
sticks_Q_label = Label(page1, text="Кол-во: ", bg='white', fg='black', font='Calibri')
sticks_Q_label.place(x=180, y=470)
hover(sticks_cart_button, on_entrance='#0E76A9', on_exit='black', entrance_fg='white', exit_fg='white')

sticks_cart_button.place(x=450, y=465)

hover(sticks_cart_button, on_entrance='#0E76A9', on_exit='black', entrance_fg='white', exit_fg='white')

fingers_label = Label(page1, text="Багет", fg='black', bg='white', font=('Calibri', 13, "bold"))
fingers_label.place(x=25, y=510)

fingers_var = IntVar()
fingers_var.set(0)
fingers_Q = Entry(page1, highlightbackground='black', highlightthickness=4, textvariable=fingers_var)
fingers_Q.place(x=250, y=510)

fingers_Q_label = Label(page1, text="Кол-во: ", bg='white', fg='black', font='Calibri')
fingers_Q_label.place(x=180, y=510)

fingers_cart_button = Button(page1, text='$4.55', relief=FLAT,
                             command=tb, bg='black', fg='white', font='Calibri')
fingers_cart_button.place(x=450, y=510)
hover(fingers_cart_button, on_entrance='#0E76A9', on_exit='black', entrance_fg='white', exit_fg='white')

rice_label = Label(page2, text='Гороховый суп', bg='white', font=("Calibri", 18), fg='#0E76A9')
rice_label.place(x=250, y=1)

rice_description = Label(page2, text=
"""Для пранков над соседями в общаге""",
                         bg='white', fg='#0E76A9', font=('Calibri', 13))
rice_description.place(x=100, y=35)

rice_price = Label(page2, text=' $8.45', font=('Calibri', 15, "bold"), bg='white', fg='#0E76A9')
rice_price.place(x=520, y=80)

rice_cart_button = Button(page2, text='В корзину', font='Calibri', bg='#0E76A9', fg='white', relief=FLAT,
                          command=tb)
rice_cart_button.place(x=25, y=80)
hover(rice_cart_button, on_entrance='black', entrance_fg='white', on_exit='#0E76A9', exit_fg='white')

rice_Var = IntVar()
rice_Var.set("0")
rice_Q = Entry(page2, highlightbackground='#0E76A9', highlightthickness=4, textvariable=rice_Var)
rice_Q.place(x=250, y=80)
rice_Q_label = Label(page2, text='Кол-во: ', bg='white', fg='#0E76A9', font=('Calibri', 12))
rice_Q_label.place(x=180, y=80)

Label(page2, text=line + '_________________', bg='white').place(x=1, y=120)

chops_label = Label(page2, text='Котлета из отчисленного', bg='white', font=("Calibri", 18), fg='black')
chops_label.place(x=200, y=140)

chops_description = Label(page2, text=
"""Неправильно оформил титульник""",
                          bg='white', fg='black', font=('Calibri', 13))
chops_description.place(x=150, y=175)

chops_price = Label(page2, text=' $8.75', font=('Calibri', 15, "bold"), bg='white', fg='black')
chops_price.place(x=520, y=220)

chops_cart_button = Button(page2, text='В корзину', font='Calibri', bg='black', fg='white', relief=FLAT, command=tb)
chops_cart_button.place(x=25, y=220)
hover(chops_cart_button, on_entrance='#0E76A9', entrance_fg='white', on_exit='black', exit_fg='white')

chops_var = IntVar()
chops_var.set(0)
chops_Q = Entry(page2, highlightbackground='black', highlightthickness=4, textvariable=chops_var)
chops_Q.place(x=250, y=220)
chops_Q_label = Label(page2, text='Кол-во: ', bg='white', fg='black', font=('Calibri', 12))
chops_Q_label.place(x=180, y=220)

Label(page2, text=line + '_________________', bg='white').place(x=1, y=260)

meatloaf_label = Label(page2, text='Сосиски из индусов', bg='white', font=("Calibri", 18), fg='#0E76A9')
meatloaf_label.place(x=170, y=285)

meatloaf_description = Label(page2, text=
"""Любимое блюдо Каира""",
                             bg='white', fg='#0E76A9', font=('Calibri', 13))
meatloaf_description.place(x=130, y=320)

meatloaf_price = Label(page2, text=' $7.60', font=('Calibri', 15, "bold"), bg='white', fg='#0E76A9')
meatloaf_price.place(x=520, y=370)

meatloaf_cart_button = Button(page2, text='В корзину', font='Calibri', bg='#0E76A9', fg='white', relief=FLAT,
                              command=tb)
meatloaf_cart_button.place(x=25, y=370)
hover(meatloaf_cart_button, on_entrance='black', entrance_fg='white', on_exit='#0E76A9', exit_fg='white')

meatloaf_var = IntVar()
meatloaf_var.set(0)
meatloaf_Q = Entry(page2, highlightbackground='black', highlightthickness=4, textvariable=meatloaf_var)
meatloaf_Q.place(x=250, y=370)
meatloaf_Q_label = Label(page2, text='Кол-во: ', bg='white', fg='#0E76A9', font=('Calibri', 12))
meatloaf_Q_label.place(x=180, y=370)

Label(page2, text=line + '_________________', bg='white', fg='black').place(x=1, y=400)

Label(page2, text='Другое', bg='white', fg='black', font=("Calibri", 15, "bold")).place(x=250, y=430)

salmon_label = Label(page2, text="Обед первокурсника", fg='black', bg='white', font=('Calibri', 13, "bold"))
salmon_label.place(x=25, y=470)
salmon_cart_button = Button(page2, text='$6.50', relief=FLAT,
                            command=tb, bg='black', fg='white', font='Calibri')
salmon_cart_button.place(x=450, y=465)

salmon_var = IntVar()

salmon_Q = Entry(page2, highlightbackground='black', highlightthickness=4, textvariable=salmon_var)
salmon_Q.place(x=250, y=470)
salmon_Q_label = Label(page2, text="Кол-во: ", bg='white', fg='black', font='Calibri')
salmon_Q_label.place(x=180, y=470)
hover(salmon_cart_button, on_entrance='#0E76A9', on_exit='black', entrance_fg='white', exit_fg='white')

tuna_label = Label(page2, text="Голубцы из голубей", fg='black', bg='white', font=('Calibri', 13, "bold"))
tuna_label.place(x=25, y=510)

tuna_var = IntVar()
tuna_var.set(0)
tuna_Q = Entry(page2, highlightbackground='black', highlightthickness=4, textvariable=tuna_var)
tuna_Q.place(x=250, y=510)

tuna_Q_label = Label(page2, text="Кол-во: ", bg='white', fg='black', font='Calibri')
tuna_Q_label.place(x=180, y=510)

tuna_cart_button = Button(page2, text='$8.90', relief=FLAT,
                          command=tb, bg='black', fg='white', font='Calibri')
tuna_cart_button.place(x=450, y=510)
hover(tuna_cart_button, on_entrance='#0E76A9', on_exit='black', entrance_fg='white', exit_fg='white')

mushroom_label = Label(page3, text='Салат студенческий', bg='white', font=("Calibri", 18), fg='#0E76A9')
mushroom_label.place(x=200, y=1)

mushroom_description = Label(page3, text=
"""Не сдал Колесникова""",
                             bg='white', fg='#0E76A9', font=('Calibri', 13))
mushroom_description.place(x=100, y=35)

mushroom_price = Label(page3, text=' $7.50', font=('Calibri', 15, "bold"), bg='white', fg='#0E76A9')
mushroom_price.place(x=520, y=80)

mushroom_cart_button = Button(page3, text='В корзину', font='Calibri', bg='#0E76A9', fg='white', relief=FLAT,
                              command=tb)
mushroom_cart_button.place(x=25, y=80)
hover(mushroom_cart_button, on_entrance='black', entrance_fg='white', on_exit='#0E76A9', exit_fg='white')

mushroom_Var = IntVar()
mushroom_Var.set("0")
mushroom_Q = Entry(page3, highlightbackground='#0E76A9', highlightthickness=4, textvariable=mushroom_Var)
mushroom_Q.place(x=250, y=80)
mushroom_Q_label = Label(page3, text='Кол-во: ', bg='white', fg='#0E76A9', font=('Calibri', 12))
mushroom_Q_label.place(x=180, y=80)

Label(page3, text=line + '_________________', bg='white').place(x=1, y=120)

cauliflower_label = Label(page3, text='Салат студенческий для платников', bg='white', font=("Calibri", 18), fg='black')
cauliflower_label.place(x=200, y=140)

cauliflower_description = Label(page3, text=
"""Тот же самый салат студенческий, но подороже""",
                                bg='white', fg='black', font=('Calibri', 13))
cauliflower_description.place(x=150, y=175)

cauliflower_price = Label(page3, text=' $7.30', font=('Calibri', 15, "bold"), bg='white', fg='black')
cauliflower_price.place(x=520, y=220)

cauliflower_cart_button = Button(page3, text='В корзину', font='Calibri', bg='black', fg='white', relief=FLAT,
                                 command=tb)
cauliflower_cart_button.place(x=25, y=220)
hover(cauliflower_cart_button, on_entrance='#0E76A9', entrance_fg='white', on_exit='black', exit_fg='white')

cauliflower_var = IntVar()
cauliflower_var.set(0)
cauliflower_Q = Entry(page3, highlightbackground='black', highlightthickness=4, textvariable=cauliflower_var)
cauliflower_Q.place(x=250, y=220)
cauliflower_Q_label = Label(page3, text='Кол-во: ', bg='white', fg='black', font=('Calibri', 12))
cauliflower_Q_label.place(x=180, y=220)

Label(page3, text=line + '_________________', bg='white').place(x=1, y=260)

macaroni_label = Label(page3, text='Салат ультра люкс плюс', bg='white', font=("Calibri", 18), fg='#0E76A9')
macaroni_label.place(x=170, y=285)

macaroni_description = Label(page3, text=
"""Тот же самый салат для платников, но еще дороже""",
                             bg='white', fg='#0E76A9', font=('Calibri', 13))
macaroni_description.place(x=160, y=320)

macaroni_price = Label(page3, text=' $5.0', font=('Calibri', 15, "bold"), bg='white', fg='#0E76A9')
macaroni_price.place(x=520, y=370)

macaroni_cart_button = Button(page3, text='В корзину', font='Calibri', bg='#0E76A9', fg='white', relief=FLAT,
                              command=tb)
macaroni_cart_button.place(x=25, y=370)
hover(macaroni_cart_button, on_entrance='black', entrance_fg='white', on_exit='#0E76A9', exit_fg='white')

macaroni_var = IntVar()
macaroni_var.set(0)
macaroni_Q = Entry(page3, highlightbackground='black', highlightthickness=4, textvariable=macaroni_var)
macaroni_Q.place(x=250, y=370)
macaroni_Q_label = Label(page3, text='Кол-во: ', bg='white', fg='#0E76A9', font=('Calibri', 12))
macaroni_Q_label.place(x=180, y=370)

Label(page3, text=line + '_________________', bg='white', fg='black').place(x=1, y=400)

Label(page3, text='Другое', bg='white', fg='black', font=("Calibri", 15, "bold")).place(x=250, y=430)

noodles_label = Label(page3, text="Вилка", fg='black', bg='white', font=('Calibri', 13, "bold"))
noodles_label.place(x=25, y=470)
noodles_cart_button = Button(page3, text='$7.75', relief=FLAT,
                             command=tb, bg='black', fg='white', font='Calibri')
noodles_cart_button.place(x=450, y=465)

noodles_var = IntVar()

noodles_Q = Entry(page3, highlightbackground='black', highlightthickness=4, textvariable=noodles_var)
noodles_Q.place(x=250, y=470)
noodles_Q_label = Label(page3, text="Кол-во: ", bg='white', fg='black', font='Calibri')
noodles_Q_label.place(x=180, y=470)
hover(noodles_cart_button, on_entrance='#0E76A9', on_exit='black', entrance_fg='white', exit_fg='white')

sandwich_label = Label(page3, text="Цена к салату", fg='black', bg='white', font=('Calibri', 13, "bold"))
sandwich_label.place(x=25, y=510)

sandwich_var = IntVar()
sandwich_var.set(0)
sandwich_Q = Entry(page3, highlightbackground='black', highlightthickness=4, textvariable=sandwich_var)
sandwich_Q.place(x=250, y=510)

sandwich_Q_label = Label(page3, text="Кол-во: ", bg='white', fg='black', font='Calibri')
sandwich_Q_label.place(x=180, y=510)

sandwich_cart_button = Button(page3, text='$3.50', relief=FLAT,
                              command=tb, bg='black', fg='white', font='Calibri')
sandwich_cart_button.place(x=450, y=510)
hover(sandwich_cart_button, on_entrance='#0E76A9', on_exit='black', entrance_fg='white', exit_fg='white')

cake_label = Label(page4, text='Муха в шоколаде', bg='white', font=("Calibri", 18), fg='#0E76A9')
cake_label.place(x=250, y=1)

cake_description = Label(page4, text="""Мухи с подоконника туалета""",
                         bg='white', fg='#0E76A9', font=('Calibri', 13))
cake_description.place(x=120, y=35)

cake_price = Label(page4, text=' $10.0', font=('Calibri', 15, "bold"), bg='white', fg='#0E76A9')
cake_price.place(x=520, y=80)

cake_cart_button = Button(page4, text='В корзину', font='Calibri', bg='#0E76A9', fg='white', relief=FLAT,
                          command=tb)
cake_cart_button.place(x=25, y=80)
hover(cake_cart_button, on_entrance='black', entrance_fg='white', on_exit='#0E76A9', exit_fg='white')

cake_Var = IntVar()
cake_Var.set("0")
cake_Q = Entry(page4, highlightbackground='#0E76A9', highlightthickness=4, textvariable=cake_Var)
cake_Q.place(x=250, y=80)
cake_Q_label = Label(page4, text='Кол-во: ', bg='white', fg='#0E76A9', font=('Calibri', 12))
cake_Q_label.place(x=180, y=80)

Label(page4, text=line + '_________________', bg='white').place(x=1, y=120)

apple_label = Label(page4, text='Селедка в шубе из ЦУМа', bg='white', font=("Calibri", 18), fg='black')
apple_label.place(x=200, y=140)

apple_description = Label(page4, text=
"""Шуба арегинал атвечаю""",
                          bg='white', fg='black', font=('Calibri', 13))
apple_description.place(x=185, y=175)

apple_price = Label(page4, text=' $5.00', font=('Calibri', 15, "bold"), bg='white', fg='black')
apple_price.place(x=520, y=220)

apple_cart_button = Button(page4, text='В корзину', font='Calibri', bg='black', fg='white', relief=FLAT,
                           command=tb)
apple_cart_button.place(x=25, y=220)
hover(apple_cart_button, on_entrance='#0E76A9', entrance_fg='white', on_exit='black', exit_fg='white')

apple_var = IntVar()
apple_var.set(0)
apple_Q = Entry(page4, highlightbackground='black', highlightthickness=4, textvariable=apple_var)
apple_Q.place(x=250, y=220)
apple_Q_label = Label(page4, text='Кол-во: ', bg='white', fg='black', font=('Calibri', 12))
apple_Q_label.place(x=180, y=220)

Label(page4, text=line + '_________________', bg='white').place(x=1, y=260)

split_label = Label(page4, text='Банан', bg='white', font=("Calibri", 18), fg='#0E76A9')
split_label.place(x=200, y=285)

split_description = Label(page4, text=
"""Среднестатистический желтый банан""",
                          bg='white', fg='#0E76A9', font=('Calibri', 13))
split_description.place(x=160, y=320)

split_price = Label(page4, text=' $8.25', font=('Calibri', 15, "bold"), bg='white', fg='#0E76A9')
split_price.place(x=520, y=370)

split_cart_button = Button(page4, text='В корзину', font='Calibri', bg='#0E76A9', fg='white', relief=FLAT,
                           command=tb)
split_cart_button.place(x=25, y=370)
hover(split_cart_button, on_entrance='black', entrance_fg='white', on_exit='#0E76A9', exit_fg='white')

split_var = IntVar()
split_var.set(0)
split_Q = Entry(page4, highlightbackground='black', highlightthickness=4, textvariable=split_var)
split_Q.place(x=250, y=370)
split_Q_label = Label(page4, text='Кол-во: ', bg='white', fg='#0E76A9', font=('Calibri', 12))
split_Q_label.place(x=180, y=370)

Label(page4, text=line + '_________________', bg='white', fg='black').place(x=1, y=400)

Label(page4, text='Другое', bg='white', fg='black', font=("Calibri", 15, "bold")).place(x=250, y=430)

cream_pie_label = Label(page4, text="Ложка", fg='black', bg='white', font=('Calibri', 13, "bold"))
cream_pie_label.place(x=25, y=470)
cream_pie_cart_button = Button(page4, text='$6.10', relief=FLAT,
                               command=tb, bg='black', fg='white', font='Calibri')
cream_pie_cart_button.place(x=450, y=465)

cream_pie_var = IntVar()

cream_pie_Q = Entry(page4, highlightbackground='black', highlightthickness=4, textvariable=cream_pie_var)
cream_pie_Q.place(x=250, y=470)
cream_pie_Q_label = Label(page4, text="Кол-во: ", bg='white', fg='black', font='Calibri')
cream_pie_Q_label.place(x=180, y=470)
hover(cream_pie_cart_button, on_entrance='#0E76A9', on_exit='black', entrance_fg='white', exit_fg='white')

pudding_label = Label(page4, text="Соль", fg='black', bg='white', font=('Calibri', 13, "bold"))
pudding_label.place(x=25, y=510)

pudding_var = IntVar()
pudding_var.set(0)
pudding_Q = Entry(page4, highlightbackground='black', highlightthickness=4, textvariable=pudding_var)
pudding_Q.place(x=250, y=510)

pudding_Q_label = Label(page4, text="Кол-во: ", bg='white', fg='black', font='Calibri')
pudding_Q_label.place(x=180, y=510)

pudding_cart_button = Button(page4, text='$5.55', relief=FLAT,
                             command=tb, bg='black', fg='white', font='Calibri')
pudding_cart_button.place(x=450, y=510)
hover(pudding_cart_button, on_entrance='#0E76A9', on_exit='black', entrance_fg='white', exit_fg='white')

cold_label = Label(page5, text='Квас', bg='white', font=("Calibri", 18), fg='#0E76A9')
cold_label.place(x=200, y=1)

cold_description = Label(page5, text=
"""Свежий квас в пивной кружке""",
                         bg='white', fg='#0E76A9', font=('Calibri', 13))
cold_description.place(x=180, y=35)

cold_price = Label(page5, text=' $3.50', font=('Calibri', 15, "bold"), bg='white', fg='#0E76A9')
cold_price.place(x=520, y=80)

cold_cart_button = Button(page5, text='В корзину', font='Calibri', bg='#0E76A9', fg='white', relief=FLAT,
                          command=tb)
cold_cart_button.place(x=25, y=80)
hover(cold_cart_button, on_entrance='black', entrance_fg='white', on_exit='#0E76A9', exit_fg='white')

cold_Var = IntVar()
cold_Var.set("0")
cold_Q = Entry(page5, highlightbackground='#0E76A9', highlightthickness=4, textvariable=cold_Var)
cold_Q.place(x=250, y=80)
cold_Q_label = Label(page5, text='Кол-во: ', bg='white', fg='#0E76A9', font=('Calibri', 12))
cold_Q_label.place(x=180, y=80)

Label(page5, text=line + '_________________', bg='white').place(x=1, y=120)

strawberry_label = Label(page5, text='Слезы четверокурсников', bg='white', font=("Calibri", 18), fg='black')
strawberry_label.place(x=200, y=140)

strawberry_description = Label(page5, text=
"""Экзамены...........""",
                               bg='white', fg='black', font=('Calibri', 13))
strawberry_description.place(x=185, y=175)

strawberry_price = Label(page5, text=' $3.00', font=('Calibri', 15, "bold"), bg='white', fg='black')
strawberry_price.place(x=520, y=220)

strawberry_cart_button = Button(page5, text='В корзину', font='Calibri', bg='black', fg='white', relief=FLAT,
                                command=tb)
strawberry_cart_button.place(x=25, y=220)
hover(strawberry_cart_button, on_entrance='#0E76A9', entrance_fg='white', on_exit='black', exit_fg='white')

strawberry_var = IntVar()
strawberry_var.set(0)
strawberry_Q = Entry(page5, highlightbackground='black', highlightthickness=4, textvariable=strawberry_var)
strawberry_Q.place(x=250, y=220)
strawberry_Q_label = Label(page5, text='Кол-во: ', bg='white', fg='black', font=('Calibri', 12))
strawberry_Q_label.place(x=180, y=220)

Label(page5, text=line + '_________________', bg='white').place(x=1, y=260)

watermelon_label = Label(page5, text='Мои слезы', bg='white', font=("Calibri", 18), fg='#0E76A9')
watermelon_label.place(x=200, y=285)

watermelon_description = Label(page5, text=
"""Я устал""",
                               bg='white', fg='#0E76A9', font=('Calibri', 13))
watermelon_description.place(x=160, y=320)

watermelon_price = Label(page5, text=' $2.70', font=('Calibri', 15, "bold"), bg='white', fg='#0E76A9')
watermelon_price = Label(page5, text=' $2.70', font=('Calibri', 15, "bold"), bg='white', fg='#0E76A9')
watermelon_price.place(x=520, y=370)

watermelon_cart_button = Button(page5, text='В корзину', font='Calibri', bg='#0E76A9', fg='white', relief=FLAT,
                                command=tb)
watermelon_cart_button.place(x=25, y=370)
hover(watermelon_cart_button, on_entrance='black', entrance_fg='white', on_exit='#0E76A9', exit_fg='white')

watermelon_var = IntVar()
watermelon_var.set(0)
watermelon_Q = Entry(page5, highlightbackground='black', highlightthickness=4, textvariable=watermelon_var)
watermelon_Q.place(x=250, y=370)
watermelon_Q_label = Label(page5, text='Кол-во: ', bg='white', fg='#0E76A9', font=('Calibri', 12))
watermelon_Q_label.place(x=180, y=370)

Label(page5, text=line + '_________________', bg='white', fg='black').place(x=1, y=400)

Label(page5, text='Другое', bg='white', fg='black', font=("Calibri", 15, "bold")).place(x=250, y=430)

tea_label = Label(page5, text="Стакан", fg='black', bg='white', font=('Calibri', 13, "bold"))
tea_label.place(x=25, y=470)
tea_cart_button = Button(page5, text='$2.00', relief=FLAT,
                         command=tb, bg='black', fg='white', font='Calibri')
tea_cart_button.place(x=450, y=465)

tea_var = IntVar()
tea_var.set(0)
tea_Q = Entry(page5, highlightbackground='black', highlightthickness=4, textvariable=tea_var)
tea_Q.place(x=250, y=470)
tea_Q_label = Label(page5, text="Кол-во: ", bg='white', fg='black', font='Calibri')
tea_Q_label.place(x=180, y=470)
hover(tea_cart_button, on_entrance='#0E76A9', on_exit='black', entrance_fg='white', exit_fg='white')

coffee_label = Label(page5, text="Перец", fg='black', bg='white', font=('Calibri', 13, "bold"))
coffee_label.place(x=25, y=510)

coffee_var = IntVar()
coffee_var.set(0)
coffee_Q = Entry(page5, highlightbackground='black', highlightthickness=4, textvariable=coffee_var)
coffee_Q.place(x=250, y=510)

coffee_Q_label = Label(page5, text="Кол-во: ", bg='white', fg='black', font='Calibri')
coffee_Q_label.place(x=180, y=510)

coffee_cart_button = Button(page5, text='$2.00', relief=FLAT,
                            command=tb, bg='black', fg='white', font='Calibri')
coffee_cart_button.place(x=450, y=510)
hover(coffee_cart_button, on_entrance='#0E76A9', on_exit='black', entrance_fg='white', exit_fg='white')

cart_button = Button(root, text='Корзина', font=('Arial', 9), bg='#0E76A9', fg='white', width=17, height=6,
                     relief=FLAT, command=tb)
hover(cart_button, on_entrance='black', on_exit='#0E76A9', entrance_fg='white', exit_fg='white')
cart_button.place(x=0, y=50)

buy_button = Button(root, text='Заказать', font=('Arial', 9), bg='#0E76A9', fg='white', width=17, height=6, relief=FLAT,
                    command=tb)
hover(buy_button, on_entrance='black', on_exit='#0E76A9', entrance_fg='white', exit_fg='white')
buy_button.place(x=0, y=160)

sign_out_button = Button(root, text='Выход', font=('Arial', 9), bg='#0E76A9', fg='white', width=17, height=6,
                         relief=FLAT, command=sign_out)
hover(sign_out_button, on_entrance='black', on_exit='#0E76A9', entrance_fg='white', exit_fg='white')
sign_out_button.place(x=0, y=270)

about_button = Button(root, text='О нас', font=('Arial', 9), bg='#0E76A9', fg='white', width=17, height=6,
                      relief=FLAT, command=about)
hover(about_button, on_entrance='black', on_exit='#0E76A9', entrance_fg='white', exit_fg='white')
about_button.place(x=0, y=380)

exit_button = Button(root, text='Выход', font=('Arial', 9), bg='#D50404', fg='white', width=17, height=6, relief=FLAT,
                     command=quit_app)
hover(exit_button, on_entrance='black', on_exit='#D50404', entrance_fg='white', exit_fg='white')
exit_button.place(x=0, y=490)

root.protocol("WM_DELETE_WINDOW", quit_app)
signup_box()
root.mainloop()
