# POST /begin

This endpoint creates a new game on the server side, and returns game information.
This endpoint is the equivalent to the `begin_game` function in `controller_go_fish.py`.

## Request Parameters

| Field         | Type         | Default             | Usage                                                                                           |
|---------------|--------------|---------------------|-------------------------------------------------------------------------------------------------|
| playerName    | string       | Player              | The name of the human player                                                                    |
| numBots       | int          | 3                   | The number of bots for the player to play against                                               |
| botNames      | List[string] | [Bot 1, Bot 2, ...] | The names for each of the bots. The length of this list must be >= the number of bots parameter |
| botDifficulty | int          | 0                   | The difficulty of the bots to play against. Must be 0, 1 or 2.                                  |

## Response Parameters

| Type   | Notes                                                           |
|--------|-----------------------------------------------------------------|
| string | Game Key. Used for all subsequent requests to identify the game |

## Errors

**400**: If there was an error with the request syntax or errors in the request values  
**500**: If there was some error processing the request  

## Notes

This endpoint makes the most sense as a POST request, as it is adding new information to the server.

# PUT /askcard

This endpoint asks for a card from a bot for the player.
This endpoint is the equivalent to the `human_ask` function in `controller_go_fish.py`.

## Request Parameters

| Field   | Type         | Default  | Usage                     |
|---------|--------------|----------|---------------------------|
| gameKey | string       | Required | The game key              |
| card    | Card         | Required | the card to match against |
| bot     | List[string] | Required | the ID of the bot to ask  |

## Response Parameters

| Type | Notes                                                                                 |
|------|---------------------------------------------------------------------------------------|
| Card | This will be the card that was received from the bot, or null if they didn't have one |

## Errors

**400**: If there was an error with the request syntax, there were missing values or errors in the request values  
**401**: If the game key is invalid  
**500**: If there was some error processing the request  

## Notes

This endpoint makes the most sense as a PUT request as the user is modifying a resource on the server.

# GET /playerinfo

This endpoint returns the human player's hand so it can be displayed to the user.

## Request Parameters

| Field   | Type   | Default  | Usage        |
|---------|--------|----------|--------------|
| gameKey | string | Required | The game key |

## Response Parameters

| Type             | Notes                                         |
|------------------|-----------------------------------------------|
| List[Card]       | A list of all the card's in the player's hand |
| List[List[Card]] | A list of pairs of cards                      |
| int              | The player's score                            |

## Errors

**400**: If there was an error with the request syntax, there were missing values or errors in the request values  
**401**: If the game key is invalid  
**500**: If there was some error processing the request  

## Notes

This endpoint makes the most sense as a GET request as it is simply retrieving information from the server.

# GET /output

This endpoint returns the output for all the players. This includes messages for the bots as well, so the player knows what has occurred.

## Request Parameters

| Field   | Type   | Default  | Usage        |
|---------|--------|----------|--------------|
| gameKey | string | Required | The game key |

## Response Parameters

| Type               | Notes                                                                             |
|--------------------|-----------------------------------------------------------------------------------|
| List[List[string]] | A list, containing a list of each player and bot's output since the last request. |

## Errors

**400**: If there was an error with the request syntax, there were missing values or errors in the request values  
**401**: If the game key is invalid  
**500**: If there was some error processing the request  

## Notes

This endpoint makes the most sense as a GET request as it is simply retrieving information from the server.


# GET /botinfo

This endpoint returns information on each of the bots, including pairs, hand size and score.

## Request Parameters

| Field   | Type   | Default  | Usage        |
|---------|--------|----------|--------------|
| gameKey | string | Required | The game key |

## Response Parameters

| Type                   | Notes                                                                             |
|------------------------|-----------------------------------------------------------------------------------|
| List[List[string]]     | A list, containing a list of each player and bot's output since the last request. |
| List[List[List[Card]]] | A list of pairs of cards for each bot                                             |
| List[int]              | Each bot's score                                                                  |
| List[int]              | The size of each bot's hand                                                       |

## Errors

**400**: If there was an error with the request syntax, there were missing values or errors in the request values  
**401**: If the game key is invalid  
**500**: If there was some error processing the request  

## Notes

This endpoint makes the most sense as a GET request as it is simply retrieving information from the server.

# GET /deckinfo

This endpoint returns information on each of the bots, including pairs, hand size and score.

## Request Parameters

| Field   | Type   | Default  | Usage        |
|---------|--------|----------|--------------|
| gameKey | string | Required | The game key |

## Response Parameters

| Type | Notes                                     |
|------|-------------------------------------------|
| int  | the number of cards remaining in the deck |

## Errors

**400**: If there was an error with the request syntax, there were missing values or errors in the request values  
**401**: If the game key is invalid  
**500**: If there was some error processing the request  

## Notes

This endpoint makes the most sense as a GET request as it is simply retrieving information from the server.
