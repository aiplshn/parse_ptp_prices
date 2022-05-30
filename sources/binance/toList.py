def toList(data):
    return {
            "Tinkoff": 
            {
            "USDT":
            {
                "BUY": 
                {
                    "few": float(data['sheets'][0]['data'][0]["rowData"][2]['values'][2]['userEnteredValue']['numberValue']),
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][2]['values'][3]['userEnteredValue']['numberValue'])
                },
                "SELL":
                {
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][2]['values'][4]['userEnteredValue']['numberValue']),
                    "few": float(data['sheets'][0]['data'][0]["rowData"][2]['values'][5]['userEnteredValue']['numberValue'])
                }
            },
            "BTC":
            {
                "BUY": 
                {
                    "few": float(data['sheets'][0]['data'][0]["rowData"][3]['values'][2]['userEnteredValue']['numberValue']),
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][3]['values'][3]['userEnteredValue']['numberValue'])
                },
                "SELL":
                {
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][3]['values'][4]['userEnteredValue']['numberValue']),
                    "few": float(data['sheets'][0]['data'][0]["rowData"][3]['values'][5]['userEnteredValue']['numberValue'])
                }
            },
            "BUSD":
            {
                "BUY": 
                {
                    "few": float(data['sheets'][0]['data'][0]["rowData"][4]['values'][2]['userEnteredValue']['numberValue']),
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][4]['values'][3]['userEnteredValue']['numberValue'])
                },
                "SELL":
                {
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][4]['values'][4]['userEnteredValue']['numberValue']),
                    "few": float(data['sheets'][0]['data'][0]["rowData"][4]['values'][5]['userEnteredValue']['numberValue'])
                }
            },
            "BNB":
            {
                "BUY": 
                {
                    "few": float(data['sheets'][0]['data'][0]["rowData"][5]['values'][2]['userEnteredValue']['numberValue']),
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][5]['values'][3]['userEnteredValue']['numberValue'])
                },
                "SELL":
                {
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][5]['values'][4]['userEnteredValue']['numberValue']),
                    "few": float(data['sheets'][0]['data'][0]["rowData"][5]['values'][5]['userEnteredValue']['numberValue'])
                }
            },
            "ETH":
            {
                "BUY": 
                {
                    "few": float(data['sheets'][0]['data'][0]["rowData"][6]['values'][2]['userEnteredValue']['numberValue']),
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][6]['values'][3]['userEnteredValue']['numberValue'])
                },
                "SELL":
                {
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][6]['values'][4]['userEnteredValue']['numberValue']),
                    "few": float(data['sheets'][0]['data'][0]["rowData"][6]['values'][5]['userEnteredValue']['numberValue'])
                }
            },
            "RUB":
            {
                "BUY": 
                {
                    "few": float(data['sheets'][0]['data'][0]["rowData"][7]['values'][2]['userEnteredValue']['numberValue']),
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][7]['values'][3]['userEnteredValue']['numberValue'])
                },
                "SELL":
                {
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][7]['values'][4]['userEnteredValue']['numberValue']),
                    "few": float(data['sheets'][0]['data'][0]["rowData"][7]['values'][5]['userEnteredValue']['numberValue'])
                }
            },
            "SHIB":
            {
                "BUY": 
                {
                    "few": float(data['sheets'][0]['data'][0]["rowData"][8]['values'][2]['userEnteredValue']['numberValue']),
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][8]['values'][3]['userEnteredValue']['numberValue'])
                },
                "SELL":
                {
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][8]['values'][4]['userEnteredValue']['numberValue']),
                    "few": float(data['sheets'][0]['data'][0]["rowData"][8]['values'][5]['userEnteredValue']['numberValue'])
                }
            }
        },

            "QIWI": 
                {
            "USDT":
            {
                "BUY": 
                {
                    "few": float(data['sheets'][0]['data'][0]["rowData"][2]['values'][6]['userEnteredValue']['numberValue']),
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][2]['values'][7]['userEnteredValue']['numberValue'])
                },
                "SELL":
                {
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][2]['values'][8]['userEnteredValue']['numberValue']),
                    "few": float(data['sheets'][0]['data'][0]["rowData"][2]['values'][9]['userEnteredValue']['numberValue'])
                }
            },
            "BTC":
            {
                "BUY": 
                {
                    "few": float(data['sheets'][0]['data'][0]["rowData"][3]['values'][6]['userEnteredValue']['numberValue']),
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][3]['values'][7]['userEnteredValue']['numberValue'])
                },
                "SELL":
                {
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][3]['values'][8]['userEnteredValue']['numberValue']),
                    "few": float(data['sheets'][0]['data'][0]["rowData"][3]['values'][9]['userEnteredValue']['numberValue'])
                }
            },
            "BUSD":
            {
                "BUY": 
                {
                    "few": float(data['sheets'][0]['data'][0]["rowData"][4]['values'][6]['userEnteredValue']['numberValue']),
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][4]['values'][7]['userEnteredValue']['numberValue'])
                },
                "SELL":
                {
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][4]['values'][8]['userEnteredValue']['numberValue']),
                    "few": float(data['sheets'][0]['data'][0]["rowData"][4]['values'][9]['userEnteredValue']['numberValue'])
                }
            },
            "BNB":
            {
                "BUY": 
                {
                    "few": float(data['sheets'][0]['data'][0]["rowData"][5]['values'][6]['userEnteredValue']['numberValue']),
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][5]['values'][7]['userEnteredValue']['numberValue'])
                },
                "SELL":
                {
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][5]['values'][8]['userEnteredValue']['numberValue']),
                    "few": float(data['sheets'][0]['data'][0]["rowData"][5]['values'][9]['userEnteredValue']['numberValue'])
                }
            },
            "ETH":
            {
                "BUY": 
                {
                    "few": float(data['sheets'][0]['data'][0]["rowData"][6]['values'][6]['userEnteredValue']['numberValue']),
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][6]['values'][7]['userEnteredValue']['numberValue'])
                },
                "SELL":
                {
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][6]['values'][8]['userEnteredValue']['numberValue']),
                    "few": float(data['sheets'][0]['data'][0]["rowData"][6]['values'][9]['userEnteredValue']['numberValue'])
                }
            },
            "RUB":
            {
                "BUY": 
                {
                    "few": float(data['sheets'][0]['data'][0]["rowData"][7]['values'][6]['userEnteredValue']['numberValue']),
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][7]['values'][7]['userEnteredValue']['numberValue'])
                },
                "SELL":
                {
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][7]['values'][8]['userEnteredValue']['numberValue']),
                    "few": float(data['sheets'][0]['data'][0]["rowData"][7]['values'][9]['userEnteredValue']['numberValue'])
                }
            },
            "SHIB":
            {
                "BUY": 
                {
                    "few": float(data['sheets'][0]['data'][0]["rowData"][8]['values'][6]['userEnteredValue']['numberValue']),
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][8]['values'][7]['userEnteredValue']['numberValue'])
                },
                "SELL":
                {
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][8]['values'][8]['userEnteredValue']['numberValue']),
                    "few": float(data['sheets'][0]['data'][0]["rowData"][8]['values'][9]['userEnteredValue']['numberValue'])
                }
            }
        },

            "YandexMoney": 
                {
            "USDT":
            {
                "BUY": 
                {
                    "few": float(data['sheets'][0]['data'][0]["rowData"][2]['values'][10]['userEnteredValue']['numberValue']),
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][2]['values'][11]['userEnteredValue']['numberValue'])
                },
                "SELL":
                {
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][2]['values'][12]['userEnteredValue']['numberValue']),
                    "few": float(data['sheets'][0]['data'][0]["rowData"][2]['values'][13]['userEnteredValue']['numberValue'])
                }
            },
            "BTC":
            {
                "BUY": 
                {
                    "few": float(data['sheets'][0]['data'][0]["rowData"][3]['values'][10]['userEnteredValue']['numberValue']),
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][3]['values'][11]['userEnteredValue']['numberValue'])
                },
                "SELL":
                {
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][3]['values'][12]['userEnteredValue']['numberValue']),
                    "few": float(data['sheets'][0]['data'][0]["rowData"][3]['values'][13]['userEnteredValue']['numberValue'])
                }
            },
            "BUSD":
            {
                "BUY": 
                {
                    "few": float(data['sheets'][0]['data'][0]["rowData"][4]['values'][10]['userEnteredValue']['numberValue']),
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][4]['values'][11]['userEnteredValue']['numberValue'])
                },
                "SELL":
                {
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][4]['values'][12]['userEnteredValue']['numberValue']),
                    "few": float(data['sheets'][0]['data'][0]["rowData"][4]['values'][13]['userEnteredValue']['numberValue'])
                }
            },
            "BNB":
            {
                "BUY": 
                {
                    "few": float(data['sheets'][0]['data'][0]["rowData"][5]['values'][10]['userEnteredValue']['numberValue']),
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][5]['values'][11]['userEnteredValue']['numberValue'])
                },
                "SELL":
                {
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][5]['values'][12]['userEnteredValue']['numberValue']),
                    "few": float(data['sheets'][0]['data'][0]["rowData"][5]['values'][13]['userEnteredValue']['numberValue'])
                }
            },
            "ETH":
            {
                "BUY": 
                {
                    "few": float(data['sheets'][0]['data'][0]["rowData"][6]['values'][10]['userEnteredValue']['numberValue']),
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][6]['values'][11]['userEnteredValue']['numberValue'])
                },
                "SELL":
                {
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][6]['values'][12]['userEnteredValue']['numberValue']),
                    "few": float(data['sheets'][0]['data'][0]["rowData"][6]['values'][13]['userEnteredValue']['numberValue'])
                }
            },
            "RUB":
            {
                "BUY": 
                {
                    "few": float(data['sheets'][0]['data'][0]["rowData"][7]['values'][10]['userEnteredValue']['numberValue']),
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][7]['values'][11]['userEnteredValue']['numberValue'])
                },
                "SELL":
                {
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][7]['values'][12]['userEnteredValue']['numberValue']),
                    "few": float(data['sheets'][0]['data'][0]["rowData"][7]['values'][13]['userEnteredValue']['numberValue'])
                }
            },
            "SHIB":
            {
                "BUY": 
                {
                    "few": float(data['sheets'][0]['data'][0]["rowData"][8]['values'][10]['userEnteredValue']['numberValue']),
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][8]['values'][11]['userEnteredValue']['numberValue'])
                },
                "SELL":
                {
                    "lot": float(data['sheets'][0]['data'][0]["rowData"][8]['values'][12]['userEnteredValue']['numberValue']),
                    "few": float(data['sheets'][0]['data'][0]["rowData"][8]['values'][13]['userEnteredValue']['numberValue'])
                }
            }
        },

            "RosBank":
            {
        "USDT":
        {
            "BUY": 
            {
                "few": float(data['sheets'][0]['data'][0]["rowData"][2]['values'][14]['userEnteredValue']['numberValue']),
                "lot": float(data['sheets'][0]['data'][0]["rowData"][2]['values'][15]['userEnteredValue']['numberValue'])
            },
            "SELL":
            {
                "lot": float(data['sheets'][0]['data'][0]["rowData"][2]['values'][16]['userEnteredValue']['numberValue']),
                "few": float(data['sheets'][0]['data'][0]["rowData"][2]['values'][17]['userEnteredValue']['numberValue'])
            }
        },
        "BTC":
        {
            "BUY": 
            {
                "few": float(data['sheets'][0]['data'][0]["rowData"][3]['values'][14]['userEnteredValue']['numberValue']),
                "lot": float(data['sheets'][0]['data'][0]["rowData"][3]['values'][15]['userEnteredValue']['numberValue'])
            },
            "SELL":
            {
                "lot": float(data['sheets'][0]['data'][0]["rowData"][3]['values'][16]['userEnteredValue']['numberValue']),
                "few": float(data['sheets'][0]['data'][0]["rowData"][3]['values'][17]['userEnteredValue']['numberValue'])
            }
        },
        "BUSD":
        {
            "BUY": 
            {
                "few": float(data['sheets'][0]['data'][0]["rowData"][4]['values'][14]['userEnteredValue']['numberValue']),
                "lot": float(data['sheets'][0]['data'][0]["rowData"][4]['values'][15]['userEnteredValue']['numberValue'])
            },
            "SELL":
            {
                "lot": float(data['sheets'][0]['data'][0]["rowData"][4]['values'][16]['userEnteredValue']['numberValue']),
                "few": float(data['sheets'][0]['data'][0]["rowData"][4]['values'][17]['userEnteredValue']['numberValue'])
            }
        },
        "BNB":
        {
            "BUY": 
            {
                "few": float(data['sheets'][0]['data'][0]["rowData"][5]['values'][14]['userEnteredValue']['numberValue']),
                "lot": float(data['sheets'][0]['data'][0]["rowData"][5]['values'][15]['userEnteredValue']['numberValue'])
            },
            "SELL":
            {
                "lot": float(data['sheets'][0]['data'][0]["rowData"][5]['values'][16]['userEnteredValue']['numberValue']),
                "few": float(data['sheets'][0]['data'][0]["rowData"][5]['values'][17]['userEnteredValue']['numberValue'])
            }
        },
        "ETH":
        {
            "BUY": 
            {
                "few": float(data['sheets'][0]['data'][0]["rowData"][6]['values'][14]['userEnteredValue']['numberValue']),
                "lot": float(data['sheets'][0]['data'][0]["rowData"][6]['values'][15]['userEnteredValue']['numberValue'])
            },
            "SELL":
            {
                "lot": float(data['sheets'][0]['data'][0]["rowData"][6]['values'][16]['userEnteredValue']['numberValue']),
                "few": float(data['sheets'][0]['data'][0]["rowData"][6]['values'][17]['userEnteredValue']['numberValue'])
            }
        },
        "RUB":
        {
            "BUY": 
            {
                "few": float(data['sheets'][0]['data'][0]["rowData"][7]['values'][14]['userEnteredValue']['numberValue']),
                "lot": float(data['sheets'][0]['data'][0]["rowData"][7]['values'][15]['userEnteredValue']['numberValue'])
            },
            "SELL":
            {
                "lot": float(data['sheets'][0]['data'][0]["rowData"][7]['values'][16]['userEnteredValue']['numberValue']),
                "few": float(data['sheets'][0]['data'][0]["rowData"][7]['values'][17]['userEnteredValue']['numberValue'])
            }
        },
        "SHIB":
        {
            "BUY": 
            {
                "few": float(data['sheets'][0]['data'][0]["rowData"][8]['values'][14]['userEnteredValue']['numberValue']),
                "lot": float(data['sheets'][0]['data'][0]["rowData"][8]['values'][15]['userEnteredValue']['numberValue'])
            },
            "SELL":
            {
                "lot": float(data['sheets'][0]['data'][0]["rowData"][8]['values'][16]['userEnteredValue']['numberValue']),
                "few": float(data['sheets'][0]['data'][0]["rowData"][8]['values'][17]['userEnteredValue']['numberValue'])
            }
        }
    },

            "RUBfiatbalance":
            {
        "USDT":
        {
            "BUY": 
            {
                "few": float(data['sheets'][0]['data'][0]["rowData"][2]['values'][18]['userEnteredValue']['numberValue']),
                "lot": float(data['sheets'][0]['data'][0]["rowData"][2]['values'][19]['userEnteredValue']['numberValue'])
            },
            "SELL":
            {
                "lot": float(data['sheets'][0]['data'][0]["rowData"][2]['values'][20]['userEnteredValue']['numberValue']),
                "few": float(data['sheets'][0]['data'][0]["rowData"][2]['values'][21]['userEnteredValue']['numberValue'])
            }
        },
        "BTC":
        {
            "BUY": 
            {
                "few": float(data['sheets'][0]['data'][0]["rowData"][3]['values'][18]['userEnteredValue']['numberValue']),
                "lot": float(data['sheets'][0]['data'][0]["rowData"][3]['values'][19]['userEnteredValue']['numberValue'])
            },
            "SELL":
            {
                "lot": float(data['sheets'][0]['data'][0]["rowData"][3]['values'][20]['userEnteredValue']['numberValue']),
                "few": float(data['sheets'][0]['data'][0]["rowData"][3]['values'][21]['userEnteredValue']['numberValue'])
            }
        },
        "BUSD":
        {
            "BUY": 
            {
                "few": float(data['sheets'][0]['data'][0]["rowData"][4]['values'][18]['userEnteredValue']['numberValue']),
                "lot": float(data['sheets'][0]['data'][0]["rowData"][4]['values'][19]['userEnteredValue']['numberValue'])
            },
            "SELL":
            {
                "lot": float(data['sheets'][0]['data'][0]["rowData"][4]['values'][20]['userEnteredValue']['numberValue']),
                "few": float(data['sheets'][0]['data'][0]["rowData"][4]['values'][21]['userEnteredValue']['numberValue'])
            }
        },
        "BNB":
        {
            "BUY": 
            {
                "few": float(data['sheets'][0]['data'][0]["rowData"][5]['values'][18]['userEnteredValue']['numberValue']),
                "lot": float(data['sheets'][0]['data'][0]["rowData"][5]['values'][19]['userEnteredValue']['numberValue'])
            },
            "SELL":
            {
                "lot": float(data['sheets'][0]['data'][0]["rowData"][5]['values'][20]['userEnteredValue']['numberValue']),
                "few": float(data['sheets'][0]['data'][0]["rowData"][5]['values'][21]['userEnteredValue']['numberValue'])
            }
        },
        "ETH":
        {
            "BUY": 
            {
                "few": float(data['sheets'][0]['data'][0]["rowData"][6]['values'][18]['userEnteredValue']['numberValue']),
                "lot": float(data['sheets'][0]['data'][0]["rowData"][6]['values'][19]['userEnteredValue']['numberValue'])
            },
            "SELL":
            {
                "lot": float(data['sheets'][0]['data'][0]["rowData"][6]['values'][20]['userEnteredValue']['numberValue']),
                "few": float(data['sheets'][0]['data'][0]["rowData"][6]['values'][21]['userEnteredValue']['numberValue'])
            }
        },
        "RUB":
        {
            "BUY": 
            {
                "few": float(data['sheets'][0]['data'][0]["rowData"][7]['values'][18]['userEnteredValue']['numberValue']),
                "lot": float(data['sheets'][0]['data'][0]["rowData"][7]['values'][19]['userEnteredValue']['numberValue'])
            },
            "SELL":
            {
                "lot": float(data['sheets'][0]['data'][0]["rowData"][7]['values'][20]['userEnteredValue']['numberValue']),
                "few": float(data['sheets'][0]['data'][0]["rowData"][7]['values'][21]['userEnteredValue']['numberValue'])
            }
        },
        "SHIB":
        {
            "BUY": 
            {
                "few": float(data['sheets'][0]['data'][0]["rowData"][8]['values'][18]['userEnteredValue']['numberValue']),
                "lot": float(data['sheets'][0]['data'][0]["rowData"][8]['values'][19]['userEnteredValue']['numberValue'])
            },
            "SELL":
            {
                "lot": float(data['sheets'][0]['data'][0]["rowData"][8]['values'][20]['userEnteredValue']['numberValue']),
                "few": float(data['sheets'][0]['data'][0]["rowData"][8]['values'][21]['userEnteredValue']['numberValue'])
            }
        }
    }
}