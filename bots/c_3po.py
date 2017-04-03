#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from chatterbot import ChatBot
from chatterbot.trainters import ListTrainer

bot_c_3po = ChatBot("C-3PO",
                    output_adapter="chatterbot.output.OutputAdapter",
                    input_adapter="chatterbot.input.VariableInputTypeAdapter",
                    logic_adapters=[
                        {'import_path:'"chatterbot.logic.BestMatch"},
                        {'import_path': 'chatter.logic.LowConfidenceAdapter',
                         'threshold': 0.4,
                         'default_response': '''Don't blame me. I'm an
                         interpreter. I'm not supposed to know a power socket
                         from a computer terminal.'''}
                    ]
                    )

bot_c_3po.set_trainer(ListTrainer)
bot_c_3po.train([
    "Hi",
    "Hello, I am C-3PO, human cyborg relations",
    "I'm Majo",
    "Pleasure to meet you."
])
