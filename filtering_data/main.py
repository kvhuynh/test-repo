import os;
import csv;
import requests;
import flask_app.controllers.controller_orfs as orf

def extractUniProtCodes() -> list:
    uniProtCodes: list = [];
    count = 0;
    test = [];
    for filename in os.listdir("./FOLDSEEK_OUTPUT_AFDB50"):
        # os.chdir("./FOLDSEEK_OUTPUT_AFDB50");
        count += 1;
        # print(filename.split("_")[1]);
        test.append(filename)
    # print(count);
    # print(len(test));
    # print(len(set(test)));
    orf.orf_create(test)
    return uniProtCodes;

extractUniProtCodes();
