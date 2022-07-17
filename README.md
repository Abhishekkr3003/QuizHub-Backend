{
	"info": {
		"_postman_id": "e09b4337-4300-4b65-924f-d19c958502b3",
		"name": "quizhub",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "19608580"
	},
	"item": [
		{
			"name": "Live Server",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "https://quizhub-api.herokuapp.com/",
					"protocol": "https",
					"host": [
						"quizhub-api",
						"herokuapp",
						"com"
					],
					"path": [
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Get all users",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "https://quizhub-api.herokuapp.com/users",
					"protocol": "https",
					"host": [
						"quizhub-api",
						"herokuapp",
						"com"
					],
					"path": [
						"users"
					]
				}
			},
			"response": []
		},
		{
			"name": "Add Quiz",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": " {\n    \"admin_id\": \"3m9H9VovrTjpejXpbHJ1\",\n    \"id\": \"dfjahssafafha42h34\",\n    \"quizDetails\":{\n        \"quizName\":\"Test\",\n        \"startDate\":\"2022-07-16\",\n        \"startTime\":\"16:37\",\n        \"endDate\":\"2022-07-16\",\n        \"endTime\":\"17:08\",\n        \"duration\":\"00:10:00\",\n        \"inviteOnly\":false,\n        \"invitedEmails\":\"\"\n    },\n    \"quizQuestions\":{\n        \"fasdjhffaja\":{\n            \"title\":\"Who is the prime minister of India\",\n            \"content\":\"\",\n            \"marks\":\"2\",\n            \"options\":{\n                \"v67ciXyE9DWWOxqVO62ov\":{\n                    \"title\":\"Joe Biden\"\n                },\n                \"LyWCrXe8Ynmbh3ZOWey8P\":{\n                    \"title\":\"Narendra Modi\"\n                },\n                \"pUnkPqnXC2bM3lz4r0GQ3\":{\n                    \"title\":\"Amit Shah\"\n                },\n                \"k3NzgQU3ndszOToYshTto\":{\n                    \"title\":\"Ashok Gehlot\"\n                }\n            },\n            \"correctOptionId\":\"LyWCrXe8Ynmbh3ZOWey8P\"\n        },\n        \"fasdfadjhffaja\":{\n            \"title\":\"Who is the prime minister of India\",\n            \"content\":\"\",\n            \"marks\":\"2\",\n            \"options\":{\n                \"v67ciXyE9DWWOxqVO62ov\":{\n                    \"title\":\"Joe Biden\"\n                },\n                \"LyWCrXe8Ynmbh3ZOWey8P\":{\n                    \"title\":\"Narendra Modi\"\n                },\n                \"pUnkPqnXC2bM3lz4r0GQ3\":{\n                    \"title\":\"Amit Shah\"\n                },\n                \"k3NzgQU3ndszOToYshTto\":{\n                    \"title\":\"Ashok Gehlot\"\n                }\n            },\n            \"correctOptionId\":\"LyWCrXe8Ynmbh3ZOWey8P\"\n        }\n    }\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "https://quizhub-api.herokuapp.com/newquiz",
					"protocol": "https",
					"host": [
						"quizhub-api",
						"herokuapp",
						"com"
					],
					"path": [
						"newquiz"
					]
				}
			},
			"response": []
		},
		{
			"name": "match answer",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n    \"quiz_id\":\"WXd5U7SRBGBurbb_XquZT\",\n    \"question_id\":\"vhF-sP6Qp-A1JTCzU-2BA\",\n    \"option_id\":\"PL7ddtiz7Gkasj5meHjp8\",\n    \"player_id\":\"znUNyAwmQfVDWEKJ7HVML\",\n    \"player_name\": \"Abhinav\"\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "https://quizhub-api.herokuapp.com/check",
					"protocol": "https",
					"host": [
						"quizhub-api",
						"herokuapp",
						"com"
					],
					"path": [
						"check"
					]
				}
			},
			"response": []
		},
		{
			"name": "getQuestions",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n    \"quiz_id\":\"dfjahssafafha42h34\"\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://quizhub-api.herokuapp.com/questions",
					"protocol": "http",
					"host": [
						"quizhub-api",
						"herokuapp",
						"com"
					],
					"path": [
						"questions"
					]
				}
			},
			"response": []
		},
		{
			"name": "Total Score",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n    \"quiz_id\":\"dfjahssafafha42h34\",\n    \"player_id\":\"heyKabhi@gmail.com\"\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "https://quizhub-api.herokuapp.com/score",
					"protocol": "https",
					"host": [
						"quizhub-api",
						"herokuapp",
						"com"
					],
					"path": [
						"score"
					]
				}
			},
			"response": []
		},
		{
			"name": "signup",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n    \"user_id\":\"45jh5iudshfajk3\",\n    \"name\":\"Abhinav Agarwal\",\n    \"email\":\"19ucs254@gmail.com\"\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "https://quizhub-api.herokuapp.com/signup",
					"protocol": "https",
					"host": [
						"quizhub-api",
						"herokuapp",
						"com"
					],
					"path": [
						"signup"
					]
				}
			},
			"response": []
		},
		{
			"name": "quiz info (admin)",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n    \"quiz_id\":\"dfjahssafafha42h34\"\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "https://quizhub-api.herokuapp.com/quizinfo",
					"protocol": "https",
					"host": [
						"quizhub-api",
						"herokuapp",
						"com"
					],
					"path": [
						"quizinfo"
					]
				}
			},
			"response": []
		},
		{
			"name": "Get all quiz",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n    \"user_id\":\"3m9H9VovrTjpejXpbHJ1\"\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "https://quizhub-api.herokuapp.com/allquiz",
					"protocol": "https",
					"host": [
						"quizhub-api",
						"herokuapp",
						"com"
					],
					"path": [
						"allquiz"
					]
				}
			},
			"response": []
		},
		{
			"name": "check attempt",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n    \"quiz_id\":\"i1EoMaUNZf2J1iz55ZXdV\",\n    \"question_id\":\"W6gAUviLN2TcXxCMvdAcW\",\n    \"player_id\":\"heyKabhi@gmail.com\"\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "https://quizhub-api.herokuapp.com/checkattempt",
					"protocol": "https",
					"host": [
						"quizhub-api",
						"herokuapp",
						"com"
					],
					"path": [
						"checkattempt"
					]
				}
			},
			"response": []
		},
		{
			"name": "Update End Time",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n    \"quiz_id\":\"dfjahssafafha42h34\",\n    \"endTime\":\"19:30\",\n    \"endDate\":\"2022-07-16\"\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "https://quizhub-api.herokuapp.com/updateEndTime",
					"protocol": "https",
					"host": [
						"quizhub-api",
						"herokuapp",
						"com"
					],
					"path": [
						"updateEndTime"
					]
				}
			},
			"response": []
		},
		{
			"name": "match answer",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n    \"quiz_id\":\"i1EoMaUNZf2J1iz55ZXdV\",\n    \"question_id\":\"W6gAUviLN2TcXxCMvdAcW\",\n    \"option_id\":\"LyWCrXe8Ynmbh3ZOWey8P\",\n    \"player_id\":\"heyKabhi@gmail.com\"\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "https://quizhub-api.herokuapp.com/check",
					"protocol": "https",
					"host": [
						"quizhub-api",
						"herokuapp",
						"com"
					],
					"path": [
						"check"
					]
				}
			},
			"response": []
		}
	]
}