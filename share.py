import sys
import os
os.system('clear')
import requests
import threading
import time
import json,requests,time
from time import strftime
from pystyle import Colorate, Colors, Write, Add, Center
def banner():
    print(f''' 
[38;2;255;255;255m╔[38;2;251;254;255m═[38;2;247;253;255m═[38;2;243;252;255m═[38;2;239;251;255m═[38;2;235;250;255m═[38;2;231;249;255m═[38;2;227;248;255m═[38;2;223;247;255m═[38;2;219;246;255m═[38;2;215;245;255m═[38;2;211;244;255m═[38;2;207;243;255m═[38;2;203;242;255m═[38;2;199;241;255m═[38;2;195;240;255m═[38;2;191;239;255m═[38;2;187;238;255m═[38;2;183;237;255m═[38;2;179;236;255m═[38;2;175;235;255m═[38;2;171;234;255m═[38;2;167;233;255m═[38;2;163;232;255m═[38;2;159;231;255m═[38;2;155;230;255m═[38;2;151;229;255m═[38;2;147;228;255m═[38;2;143;227;255m═[38;2;139;226;255m═[38;2;135;225;255m═[38;2;131;224;255m═[38;2;127;223;255m═[38;2;123;222;255m═[38;2;119;221;255m═[38;2;115;220;255m═[38;2;111;219;255m═[38;2;107;218;255m═[38;2;103;217;255m═[38;2;99;216;255m═[38;2;95;215;255m═[38;2;91;214;255m═[38;2;87;213;255m═[38;2;83;212;255m═[38;2;79;211;255m═[38;2;75;210;255m═[38;2;71;209;255m═[38;2;67;208;255m═[38;2;63;207;255m═[38;2;59;206;255m═[38;2;55;205;255m═[38;2;51;204;255m═[38;2;47;203;255m═[38;2;43;202;255m═[38;2;39;201;255m═[38;2;35;200;255m═[38;2;31;199;255m═[38;2;27;198;255m═[38;2;23;197;255m═[38;2;19;196;255m╗
[38;2;255;255;255m║[38;2;251;254;255m█[38;2;247;253;255m█[38;2;243;252;255m╗[38;2;239;251;255m [38;2;235;250;255m [38;2;231;249;255m█[38;2;227;248;255m█[38;2;223;247;255m╗[38;2;219;246;255m [38;2;215;245;255m█[38;2;211;244;255m█[38;2;207;243;255m█[38;2;203;242;255m█[38;2;199;241;255m█[38;2;195;240;255m╗[38;2;191;239;255m [38;2;187;238;255m█[38;2;183;237;255m█[38;2;179;236;255m╗[38;2;175;235;255m [38;2;171;234;255m [38;2;167;233;255m [38;2;163;232;255m [38;2;159;231;255m█[38;2;155;230;255m█[38;2;151;229;255m█[38;2;147;228;255m█[38;2;143;227;255m█[38;2;139;226;255m█[38;2;135;225;255m█[38;2;131;224;255m█[38;2;127;223;255m╗[38;2;123;222;255m [38;2;119;221;255m█[38;2;115;220;255m█[38;2;111;219;255m█[38;2;107;218;255m█[38;2;103;217;255m█[38;2;99;216;255m█[38;2;95;215;255m╗[38;2;91;214;255m [38;2;87;213;255m [38;2;83;212;255m█[38;2;79;211;255m█[38;2;75;210;255m█[38;2;71;209;255m█[38;2;67;208;255m█[38;2;63;207;255m█[38;2;59;206;255m╗[38;2;55;205;255m [38;2;51;204;255m█[38;2;47;203;255m█[38;2;43;202;255m╗[38;2;39;201;255m [38;2;35;200;255m [38;2;31;199;255m [38;2;27;198;255m [38;2;23;197;255m [38;2;19;196;255m║
[38;2;255;255;255m║[38;2;251;254;255m█[38;2;247;253;255m█[38;2;243;252;255m║[38;2;239;251;255m [38;2;235;250;255m [38;2;231;249;255m█[38;2;227;248;255m█[38;2;223;247;255m║[38;2;219;246;255m█[38;2;215;245;255m█[38;2;211;244;255m╔[38;2;207;243;255m═[38;2;203;242;255m═[38;2;199;241;255m█[38;2;195;240;255m█[38;2;191;239;255m╗[38;2;187;238;255m█[38;2;183;237;255m█[38;2;179;236;255m║[38;2;175;235;255m [38;2;171;234;255m [38;2;167;233;255m [38;2;163;232;255m [38;2;159;231;255m╚[38;2;155;230;255m═[38;2;151;229;255m═[38;2;147;228;255m█[38;2;143;227;255m█[38;2;139;226;255m╔[38;2;135;225;255m═[38;2;131;224;255m═[38;2;127;223;255m╝[38;2;123;222;255m█[38;2;119;221;255m█[38;2;115;220;255m╔[38;2;111;219;255m═[38;2;107;218;255m═[38;2;103;217;255m═[38;2;99;216;255m█[38;2;95;215;255m█[38;2;91;214;255m╗[38;2;87;213;255m█[38;2;83;212;255m█[38;2;79;211;255m╔[38;2;75;210;255m═[38;2;71;209;255m═[38;2;67;208;255m═[38;2;63;207;255m█[38;2;59;206;255m█[38;2;55;205;255m╗[38;2;51;204;255m█[38;2;47;203;255m█[38;2;43;202;255m║[38;2;39;201;255m [38;2;35;200;255m [38;2;31;199;255m [38;2;27;198;255m [38;2;23;197;255m [38;2;19;196;255m║
[38;2;255;255;255m║[38;2;251;254;255m█[38;2;247;253;255m█[38;2;243;252;255m█[38;2;239;251;255m█[38;2;235;250;255m█[38;2;231;249;255m█[38;2;227;248;255m█[38;2;223;247;255m║[38;2;219;246;255m█[38;2;215;245;255m█[38;2;211;244;255m█[38;2;207;243;255m█[38;2;203;242;255m█[38;2;199;241;255m█[38;2;195;240;255m█[38;2;191;239;255m║[38;2;187;238;255m█[38;2;183;237;255m█[38;2;179;236;255m║[38;2;175;235;255m [38;2;171;234;255m [38;2;167;233;255m [38;2;163;232;255m [38;2;159;231;255m [38;2;155;230;255m [38;2;151;229;255m [38;2;147;228;255m█[38;2;143;227;255m█[38;2;139;226;255m║[38;2;135;225;255m [38;2;131;224;255m [38;2;127;223;255m [38;2;123;222;255m█[38;2;119;221;255m█[38;2;115;220;255m║[38;2;111;219;255m [38;2;107;218;255m [38;2;103;217;255m [38;2;99;216;255m█[38;2;95;215;255m█[38;2;91;214;255m║[38;2;87;213;255m█[38;2;83;212;255m█[38;2;79;211;255m║[38;2;75;210;255m [38;2;71;209;255m [38;2;67;208;255m [38;2;63;207;255m█[38;2;59;206;255m█[38;2;55;205;255m║[38;2;51;204;255m█[38;2;47;203;255m█[38;2;43;202;255m║[38;2;39;201;255m [38;2;35;200;255m [38;2;31;199;255m [38;2;27;198;255m [38;2;23;197;255m [38;2;19;196;255m║
[38;2;255;255;255m║[38;2;251;254;255m█[38;2;247;253;255m█[38;2;243;252;255m╔[38;2;239;251;255m═[38;2;235;250;255m═[38;2;231;249;255m█[38;2;227;248;255m█[38;2;223;247;255m║[38;2;219;246;255m█[38;2;215;245;255m█[38;2;211;244;255m╔[38;2;207;243;255m═[38;2;203;242;255m═[38;2;199;241;255m█[38;2;195;240;255m█[38;2;191;239;255m║[38;2;187;238;255m█[38;2;183;237;255m█[38;2;179;236;255m║[38;2;175;235;255m [38;2;171;234;255m [38;2;167;233;255m [38;2;163;232;255m [38;2;159;231;255m [38;2;155;230;255m [38;2;151;229;255m [38;2;147;228;255m█[38;2;143;227;255m█[38;2;139;226;255m║[38;2;135;225;255m [38;2;131;224;255m [38;2;127;223;255m [38;2;123;222;255m█[38;2;119;221;255m█[38;2;115;220;255m║[38;2;111;219;255m [38;2;107;218;255m [38;2;103;217;255m [38;2;99;216;255m█[38;2;95;215;255m█[38;2;91;214;255m║[38;2;87;213;255m█[38;2;83;212;255m█[38;2;79;211;255m║[38;2;75;210;255m [38;2;71;209;255m [38;2;67;208;255m [38;2;63;207;255m█[38;2;59;206;255m█[38;2;55;205;255m║[38;2;51;204;255m█[38;2;47;203;255m█[38;2;43;202;255m║[38;2;39;201;255m [38;2;35;200;255m [38;2;31;199;255m [38;2;27;198;255m [38;2;23;197;255m [38;2;19;196;255m║
[38;2;255;255;255m║[38;2;251;254;255m█[38;2;247;253;255m█[38;2;243;252;255m║[38;2;239;251;255m [38;2;235;250;255m [38;2;231;249;255m█[38;2;227;248;255m█[38;2;223;247;255m║[38;2;219;246;255m█[38;2;215;245;255m█[38;2;211;244;255m║[38;2;207;243;255m [38;2;203;242;255m [38;2;199;241;255m█[38;2;195;240;255m█[38;2;191;239;255m║[38;2;187;238;255m█[38;2;183;237;255m█[38;2;179;236;255m║[38;2;175;235;255m [38;2;171;234;255m [38;2;167;233;255m [38;2;163;232;255m [38;2;159;231;255m [38;2;155;230;255m [38;2;151;229;255m [38;2;147;228;255m█[38;2;143;227;255m█[38;2;139;226;255m║[38;2;135;225;255m [38;2;131;224;255m [38;2;127;223;255m [38;2;123;222;255m╚[38;2;119;221;255m█[38;2;115;220;255m█[38;2;111;219;255m█[38;2;107;218;255m█[38;2;103;217;255m█[38;2;99;216;255m█[38;2;95;215;255m╔[38;2;91;214;255m╝[38;2;87;213;255m╚[38;2;83;212;255m█[38;2;79;211;255m█[38;2;75;210;255m█[38;2;71;209;255m█[38;2;67;208;255m█[38;2;63;207;255m█[38;2;59;206;255m╔[38;2;55;205;255m╝[38;2;51;204;255m█[38;2;47;203;255m█[38;2;43;202;255m█[38;2;39;201;255m█[38;2;35;200;255m█[38;2;31;199;255m█[38;2;27;198;255m█[38;2;23;197;255m╗[38;2;19;196;255m║
[38;2;255;255;255m║[38;2;251;254;255m╚[38;2;247;253;255m═[38;2;243;252;255m╝[38;2;239;251;255m [38;2;235;250;255m [38;2;231;249;255m╚[38;2;227;248;255m═[38;2;223;247;255m╝[38;2;219;246;255m╚[38;2;215;245;255m═[38;2;211;244;255m╝[38;2;207;243;255m [38;2;203;242;255m [38;2;199;241;255m╚[38;2;195;240;255m═[38;2;191;239;255m╝[38;2;187;238;255m╚[38;2;183;237;255m═[38;2;179;236;255m╝[38;2;175;235;255m [38;2;171;234;255m [38;2;167;233;255m [38;2;163;232;255m [38;2;159;231;255m [38;2;155;230;255m [38;2;151;229;255m [38;2;147;228;255m╚[38;2;143;227;255m═[38;2;139;226;255m╝[38;2;135;225;255m [38;2;131;224;255m [38;2;127;223;255m [38;2;123;222;255m [38;2;119;221;255m╚[38;2;115;220;255m═[38;2;111;219;255m═[38;2;107;218;255m═[38;2;103;217;255m═[38;2;99;216;255m═[38;2;95;215;255m╝[38;2;91;214;255m [38;2;87;213;255m [38;2;83;212;255m╚[38;2;79;211;255m═[38;2;75;210;255m═[38;2;71;209;255m═[38;2;67;208;255m═[38;2;63;207;255m═[38;2;59;206;255m╝[38;2;55;205;255m [38;2;51;204;255m╚[38;2;47;203;255m═[38;2;43;202;255m═[38;2;39;201;255m═[38;2;35;200;255m═[38;2;31;199;255m═[38;2;27;198;255m═[38;2;23;197;255m╝[38;2;19;196;255m║
[38;2;255;255;255m╚[38;2;251;254;255m═[38;2;247;253;255m═[38;2;243;252;255m═[38;2;239;251;255m═[38;2;235;250;255m═[38;2;231;249;255m═[38;2;227;248;255m═[38;2;223;247;255m═[38;2;219;246;255m═[38;2;215;245;255m═[38;2;211;244;255m═[38;2;207;243;255m═[38;2;203;242;255m═[38;2;199;241;255m═[38;2;195;240;255m═[38;2;191;239;255m═[38;2;187;238;255m═[38;2;183;237;255m═[38;2;179;236;255m═[38;2;175;235;255m═[38;2;171;234;255m═[38;2;167;233;255m═[38;2;163;232;255m═[38;2;159;231;255m═[38;2;155;230;255m═[38;2;151;229;255m═[38;2;147;228;255m═[38;2;143;227;255m═[38;2;139;226;255m═[38;2;135;225;255m═[38;2;131;224;255m═[38;2;127;223;255m═[38;2;123;222;255m═[38;2;119;221;255m═[38;2;115;220;255m═[38;2;111;219;255m═[38;2;107;218;255m═[38;2;103;217;255m═[38;2;99;216;255m═[38;2;95;215;255m═[38;2;91;214;255m═[38;2;87;213;255m═[38;2;83;212;255m═[38;2;79;211;255m═[38;2;75;210;255m═[38;2;71;209;255m═[38;2;67;208;255m═[38;2;63;207;255m═[38;2;59;206;255m═[38;2;55;205;255m═[38;2;51;204;255m═[38;2;47;203;255m═[38;2;43;202;255m═[38;2;39;201;255m═[38;2;35;200;255m═[38;2;31;199;255m═[38;2;27;198;255m═[38;2;23;197;255m═[38;2;19;196;255m╝
[38;2;255;255;255mT[38;2;250;254;255mO[38;2;245;253;255mO[38;2;240;252;255mL[38;2;235;251;255m [38;2;230;250;255mS[38;2;225;249;255mH[38;2;220;248;255mA[38;2;215;247;255mR[38;2;210;246;255mE[38;2;205;245;255m [38;2;200;244;255mẢ[38;2;195;243;255mO[38;2;190;242;255m [38;2;185;241;255mF[38;2;180;240;255mA[38;2;175;239;255mC[38;2;170;238;255mE[38;2;165;237;255mB[38;2;160;236;255mO[38;2;155;235;255mO[38;2;150;234;255mK[38;2;145;233;255m [38;2;140;232;255mM[38;2;135;231;255mA[38;2;130;230;255mX[38;2;125;229;255m [38;2;120;228;255mS[38;2;115;227;255mP[38;2;110;226;255mE[38;2;105;225;255mE[38;2;100;224;255mD[38;2;95;223;255m [38;2;90;222;255mN[38;2;85;221;255mE[38;2;80;220;255mW[38;2;75;219;255m [38;2;70;218;255m2[38;2;65;217;255m0[38;2;60;216;255m2[38;2;55;215;255m4
[38;2;255;255;255mT[38;2;230;249;254mO[38;2;205;243;253mO[38;2;180;237;252mL[38;2;155;231;251m [38;2;130;225;250mB[38;2;105;219;249mY[38;2;80;213;248m [38;2;55;207;247m: \033[1;33m@haidz2006
[38;2;255;255;255mZ[38;2;238;251;255mA[38;2;221;247;255mL[38;2;204;243;255mO[38;2;187;239;255m [38;2;170;235;255mC[38;2;153;231;255mO[38;2;136;227;255mN[38;2;119;223;255mT[38;2;102;219;255mA[38;2;85;215;255mC[38;2;68;211;255mC[38;2;51;207;255m [38;2;34;203;255m:\033[1;33m 0824117862
[0;00m''')
t=(Colorate.Horizontal(Colors.white_to_black,"- - - - - - - - - - - - - - - - - - - - - - - - -"))
print(t)
def clear():
    if(sys.platform.startswith('win')):
        os.system('cls')
    else:
        os.system('clear')
gome_token = []
def get_token(input_file):
    for cookie in input_file:
        header_ = {
            'authority': 'business.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cache-control': 'max-age=0',
            'cookie': cookie,
            'referer': 'https://www.facebook.com/',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',

        }
        try:
            home_business = requests.get('https://business.facebook.com/content_management', headers=header_).text
            token = home_business.split('EAAG')[1].split('","')[0]
            cookie_token = f'{cookie}|EAAG{token}'
            gome_token.append(cookie_token)
        except:
            pass
    return gome_token

def share(tach, id_share):
    cookie = tach.split('|')[0]
    token = tach.split('|')[1]
    he = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate',
        'connection': 'keep-alive',
        'content-length': '0',
        'cookie': cookie,
        'host': 'graph.facebook.com'
    }
    try:
        res = requests.post(f'https://graph.facebook.com/me/feed?link=https://m.facebook.com/{id_share}&published=0&access_token={token}', headers=he).json()
    except:
        pass
    
    
def main_share():
    clear()
    banner()
    input_file = open(input("[38;2;252;8;8mE[38;2;252;17;17mn[38;2;252;26;26mt[38;2;252;35;35me[38;2;252;44;44mr[38;2;252;53;53m [38;2;252;62;62mN[38;2;252;71;71ma[38;2;252;80;80mm[38;2;252;89;89me[38;2;252;98;98m [38;2;252;107;107mF[38;2;252;116;116mi[38;2;252;125;125ml[38;2;252;134;134me[38;2;252;143;143m [38;2;252;152;152mC[38;2;252;161;161mo[38;2;252;170;170mo[38;2;252;179;179mk[38;2;252;188;188mi[38;2;252;197;197me[38;2;252;206;206m [38;2;252;215;215m: \033[0m ")).read().split('\n')
    id_share = input("[38;2;252;8;8mE[38;2;252;17;17mn[38;2;252;26;26mt[38;2;252;35;35me[38;2;252;44;44mr[38;2;252;53;53m [38;2;252;62;62mI[38;2;252;71;71mD[38;2;252;80;80m [38;2;252;89;89mP[38;2;252;98;98mo[38;2;252;107;107mr[38;2;252;116;116mf[38;2;252;125;125ms[38;2;252;134;134m [38;2;252;143;143mG[38;2;252;152;152me[38;2;252;161;161mt[38;2;252;170;170m [38;2;252;179;179mS[38;2;252;188;188mh[38;2;252;197;197ma[38;2;252;206;206mr[38;2;252;215;215me[38;2;252;224;224m [38;2;252;233;233m: \033[0m ")
    delay = int(input("[38;2;252;8;8mE[38;2;252;20;20mn[38;2;252;32;32mt[38;2;252;44;44me[38;2;252;56;56mr[38;2;252;68;68m [38;2;252;80;80mD[38;2;252;92;92me[38;2;252;104;104ml[38;2;252;116;116ma[38;2;252;128;128my[38;2;252;140;140m [38;2;252;152;152mS[38;2;252;164;164mh[38;2;252;176;176ma[38;2;252;188;188mr[38;2;252;200;200me[38;2;252;212;212m [38;2;252;224;224m: \033[0m "))
    total_share = int(input("[38;2;252;8;8mT[38;2;252;19;19mo[38;2;252;30;30mt[38;2;252;41;41ma[38;2;252;52;52ml[38;2;252;63;63m [38;2;252;74;74m/[38;2;252;85;85m [38;2;252;96;96mS[38;2;252;107;107m [38;2;252;118;118mG[38;2;252;129;129me[38;2;252;140;140mt[38;2;252;151;151m [38;2;252;162;162mS[38;2;252;173;173mh[38;2;252;184;184ma[38;2;252;195;195mr[38;2;252;206;206me[38;2;252;217;217m [38;2;252;228;228m: \033[0m "))
    all = get_token(input_file)
    total_live = len(all)
    print(f'\033[0;38m────────────────────────────────────────────────────────────')
    if total_live == 0:
        sys.exit()
    stt = 0
    while True:
        for tach in all:
            stt = stt + 1
            threa = threading.Thread(target=share, args=(tach, id_share))
            threa.start()
            print(f'\033[1;33m[\033[1;37m{stt}\033[1;33m] \033[0m [38;2;255;255;255mP[38;2;246;246;254mo[38;2;237;237;253ms[38;2;228;228;252mt[38;2;219;219;251m [38;2;210;210;250mS[38;2;201;201;249mh[38;2;192;192;248ma[38;2;183;183;247mr[38;2;174;174;246me[38;2;165;165;245md[38;2;156;156;244m [38;2;147;147;243mS[38;2;138;138;242mu[38;2;129;129;241mc[38;2;120;120;240mc[38;2;111;111;239me[38;2;102;102;238ms[38;2;93;93;237ms[38;2;84;84;236mf[38;2;75;75;235mu[38;2;66;66;234ml[38;2;57;57;233ml[38;2;48;48;232my[38;2;39;39;231m! \033[1;33m[\033[1;37m{id_share}\033[1;33m]\033[0m\n', end='\r')
            time.sleep(delay)
        if stt == total_share:
            break
    gome_token.clear()
    input('Porfs Share Done! | Click " Enter " To Get Star !')
while True:
    try:
        main_share()
    except KeyboardInterrupt:
        print('\nTool By Crack And Makes By : HaiBe Developer !')
        sys.exit()