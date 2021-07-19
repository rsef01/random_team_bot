# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 00:19:03 2021

@author: rsef0
"""

import discord
import asyncio
import random

client = discord.Client()

token = "ODY2Njk5NTY5NDg0MjY3NTIw.YPWW3w.wI5h8UHudofqGTIwoAgU4hX1qnk"    

player_list = []
'''
def input_list(channel, client_list):
    input_check = 1
    @client.event
    async def on_message(message):
        if message.author.bot:
            print('봇')
            input_check = 1
        elif message.content.startswith('!완료'):# or message.content.startswith('!추가'):
            print('완료')
            await channel.send('입력완료')
            input_check = 0
        else:
            print('else')
            player_list.append(message.content)
            await channel.send('참여인원 : ' + str(client_list))
            input_check = 1
            
        return None
    return input_check
'''
'''
def remove_list(channel, client_list):
    del_check = 0
    @client.event
    async def on_message(message):
        for i in range(0, client_list.lenght):
            if client_list[i] == message.content:
                del client_list[i]
                del_check = 1
        if del_check == 0:
            await channel.send(message.content + '는 참여하지 않았습니다.')
        else : 
            await channel.send('삭제완료')
        #client_list.remove(message.content)
        return None
'''
@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")


@client.event
async def on_message(message):
    global player_list
    # 메세지를 보낸 사람이 봇일 경우 무시한다
    if message.author.bot:
        return None
    elif message.content.startswith('!입력'):
        channel = message.channel
        player_list = message.content.split(' ')
        del player_list[0]
        await channel.send(player_list)
        
    elif message.content.startswith('!팀'):
        n = 2 #나눌 리스트 갯수
        
        channel = message.channel
        random.shuffle(player_list)
        player_list_split = [player_list[i:i+n] for i in range(0, len(player_list), n)]
        for i in range(n):
            print(player_list_split)
            await channel.send(str(i+1) + '번 팀 : ' + str(player_list_split[i]))
        
    elif message.content.startswith('!도움말'):
        channel = message.channel
        await channel.send('입력예시1 : !입력 참가자1 참가자2 참가자3 ...')
        await channel.send('입력예시2 : !입력 참가자1, 참가자2, 참가자3 ...')
        await channel.send('팀나누기 : !팀')
        
    '''
    elif message.content.startswith('!입력'):# or message.content.startswith('!추가')):
        print('입력')
        client_list = []
        input_check = 1
        channel = message.channel

        await channel.send('게임에 참여할 닉네임들을 입력하세요')
        
        while(1):
            #await channel.send('input_check == 1')
            input_check = input_list(channel, client_list)
            print(str(input_check))
            if input_check != 1:
                input_check = 1
                return None
        return None
    '''
    '''
    elif message.content.startswith('!삭제'):
        channel = message.channel
        
        if client_list.length == 0:
            await channel.send('참여인원 0명. !입력을 먼저 사용해주세요')
        elif client_list.length > 0:
            await channel.send('삭제할 닉네임을 입력하세요')
            remove_list(channel, client_list)
        else:
            await channel.send('else')
        return None
    '''
    '''
    elif message.content.startswith('!추가'):
        if client_list.length == 0:
            await channel.send('인원수 0명. !입력을 먼저 사용해주세요')
            client_list.append(message.content)
            return None
    '''

    
    
'''
@client.event
async def on_message(message):
    channel = message.channel
    if message.content.startswith('!삭제'):
        await channel.send('삭제할 닉네임을 입력하세요')
        remove_list(channel, client_list, message.content)
        
    
@client.event
async def on_message(message):
    if message.content.startswith('!리셋'):
        client_list = []
    

@client.event
async def on_message(message):
    channel = message.channel
    if message.content.startswith('!도움말'):
        await channel.send('명령어 : !입력, !추가, !삭제, !리셋')
        
    '''
client.run(token)