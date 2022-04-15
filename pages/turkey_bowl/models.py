from django.db import models
import pandas as pd
import numpy as np
import boto3
from boto3.dynamodb.conditions import Key

ACCESS_KEY = "AKIARP5EWA5GEDP2EPH2"
SECRET_KEY = "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"


def get_team_list():
    team_list = pd.read_csv("pages/turkey_bowl/src_data/teams.csv")
    return {column:team_list[column].tolist() for column in team_list.columns}


def get_results(requested_round):
    dynamodb = boto3.resource('dynamodb', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, region_name="us-east-1")
    table = dynamodb.Table("2021_tourney")
    response = table.query(KeyConditionExpression=Key('round_num').eq(requested_round))
    roundGames = []
    if 'Items' in response:
        for item in response['Items']:
            roundGames.append({'round_num': int(item['round_num']), 'game': int(item['game_num']), 'winner': item['winner'], 'loser': item['loser'], 'winner_score': int(item['winner_score']), 'loser_score': int(item['loser_score'])})
    return roundGames


def insert_result(round_num, game_num, winner, loser, winner_score, loser_score):
    dynamodb = boto3.resource('dynamodb', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, region_name="us-east-1")
    table = dynamodb.Table("2021_tourney")
    table.put_item(Item={"round_num": round_num, "game_num": game_num, "winner": winner, "loser": loser, "winner_score": winner_score, "loser_score": loser_score})

