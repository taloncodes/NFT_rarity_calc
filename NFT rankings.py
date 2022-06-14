# a script used to calculate the order of rarities throughot a generative NFT collection, to use for your project insert your metadata
# then update other variables to match trait name as spelled exactly in metadata

import json
import csv
import pandas as pd

metadata = '' # <- insert NFT metadata in metaplex standard .json format

data = json.loads(metadata)
size = 353 # change for your collection size

# initialise a counter for each trait occurence (replace variable names with trait variable name in your metadata)

#   type
base1 = 0
base2 = 0
base3 = 0
base4 = 0
base5 = 0

#   body
body1 = 0
body2 = 0
body3 = 0
body4 = 0
body5 = 0

#   eyes
eyes1 = 0
eyes2 = 0
eyes3 = 0
eyes4 = 0
eyes5 = 0

#   head
head1 = 0
head2 = 0
head3 = 0
head4 = 0
head5 = 0

#   accessory
acc1 = 0
acc2 = 0
acc3 = 0
acc4 = 0
acc5 = 0

#   mouth
mouth1 = 0
mouth2 = 0
mouth3 = 0
mouth4 = 0
mouth5 = 0

#   neck
neck1 = 0
neck2 = 0
neck3 = 0
neck4 = 0
neck5 = 0

#   background
bg1 = 0
bg2 = 0
bg3 = 0
bg4 = 0
bg5 = 0

#   Find number of occurrence for each trait

for i in range(len(data)):

    attr = data[i].get("metadata").get("attributes")

    for j in range(len(attr)):
        #   background
        if (attr[j].get("value")) == "bg1":
            bg1 += 1
        elif (attr[j].get("value")) == "bg2":
            bg2 += 1
        elif (attr[j].get("value")) == "bg3":
            bg3 += 1
        elif (attr[j].get("value")) == "bg4":
            bg4 += 1
        elif (attr[j].get("value")) == "bg5":
            bg5 += 1
        #   neck
        elif (attr[j].get("value")) == "neck1":
            neck1 += 1
        elif (attr[j].get("value")) == "neck2":
            neck2 += 1
        elif (attr[j].get("value")) == "neck3":
            neck3 += 1
        elif (attr[j].get("value")) == "neck4":
            neck4 += 1
        elif (attr[j].get("value")) == "neck5":
            neck5 += 1
        #   mouth
        elif (attr[j].get("value")) == "mouth1":
            mouth1 += 1
        elif (attr[j].get("value")) == "mouth2":
            mouth2 += 1
        elif (attr[j].get("value")) == "mouth3":
            mouth3 += 1
        elif (attr[j].get("value")) == "mouth4":
            mouth4 += 1
        elif (attr[j].get("value")) == "mouth5":
            mouth5 += 1
        #   accessory
        elif (attr[j].get("value")) == "acc1":
            acc1 += 1
        elif (attr[j].get("value")) == "acc2":
            acc2 += 1
        elif (attr[j].get("value")) == "acc3":
            acc3 += 1
        elif (attr[j].get("value")) == "acc4":
            acc4 += 1
        elif (attr[j].get("value")) == "acc5":
            acc5 += 1
        #   head
        elif (attr[j].get("value")) == "head1":
            head1 += 1
        elif (attr[j].get("value")) == "head2":
            head2 += 1
        elif (attr[j].get("value")) == "head3":
            head3 += 1
        elif (attr[j].get("value")) == "head4":
            head4 += 1
        elif (attr[j].get("value")) == "head5":
            head5 += 1
        #   eyes
        elif (attr[j].get("value")) == "eyes1":
            eyes1 += 1
        elif (attr[j].get("value")) == "eyes2":
            eyes2 += 1
        elif (attr[j].get("value")) == "eyes3":
            eyes3 += 1
        elif (attr[j].get("value")) == "eyes4":
            eyes4 += 1
        elif (attr[j].get("value")) == "eyes5":
            eyes5 += 1
        
        #   body
        elif (attr[j].get("value")) == "body1":
            body1 += 1
        elif (attr[j].get("value")) == "body2":
            body2 += 1
        elif (attr[j].get("value")) == "body3":
            body3 += 1
        elif (attr[j].get("value")) == "body4":
            body4 += 1
        elif (attr[j].get("value")) == "body5":
            body5 += 1
        #   type
        elif (attr[j].get("value")) == "base1":
            base1 += 1
        elif (attr[j].get("value")) == "base2":
            base2 += 1
        elif (attr[j].get("value")) == "base3":
            base3 += 1
        elif (attr[j].get("value")) == "base4":
            base4 += 1
        elif (attr[j].get("value")) == "base5":
             base5 += 1
                 
                 
    #calculate number of NFTs with empty trait

no_neck_rarity = (size - (neck1 + neck2 + neck3 + neck4 + neck5))
no_mouth_rarity = (size - (mouth1 + mouth2 + mouth3 + mouth4 + mouth5))
no_accessory_rarity = (size - (acc1 + acc2 + acc3 + acc4 + acc5))
no_head_rarity = (size - (head1 + head2 + head3 + head4 + head5 ))
no_body_rarity = (size - (body1 + body2 + body3 + body4 + body5))

    #dict to store rarity value for each trait
trait_dict = {

    #   type
    "base1_rarity": (base1 / size) * 100,
    "base2_rarity": (base2 / size) * 100,
    "base_rarity3": (base3 / size) * 100,
    "base4_rarity": (base4 / size) * 100,
    "base5_rarity": (base5 / size) * 100,
    
    #   body
    "": (leather_jacket / size) * 100,
    "body_1_rarity": (body1 / size) * 100,
    "body_2_rarity": (body2 / size) * 100,
    "body_3_rarity": (body3 / size) * 100,
    "body_4_rarity": (body4 / size) * 100,
    "body_5_rarity": (body5 / size) * 100,

    #   eyes
    "eyes_1_rarity": (eyes1 / size) * 100,
    "eyes_2_rarity": (eyes2 / size) * 100,
    "eyes_3_rarity": (eyes3 / size) * 100,
    "eyes_4_rarity": (eyes4 / size) * 100,
    "eyes_5_rarity": (eyes5 / size) * 100,

    #   head
    "head_1_rarity": (head1 / size) * 100,
    "head_2_rarity": (head2 / size) * 100,
    "head_3_rarity": (head3 / size) * 100,
    "head_4_rarity": (head4 / size) * 100,
    "head_5_rarity": (head5 / size) * 100,    

    #   accessory
    "acc_1_rarity": (acc1 / size) * 100,
    "acc_2_rarity": (acc2 / size) * 100,
    "acc_3_rarity": (acc3 / size) * 100,
    "acc_4_rarity": (acc4 / size) * 100,
    "acc_5_rarity": (acc5 / size) * 100,


    #   mouth
    "mouth_1_rarity": (mouth1 / size) * 100,
    "mouth_2_rarity": (mouth2 / size) * 100,
    "mouth_3_rarity": (mouth3 / size) * 100,
    "mouth_4_rarity": (mouth4 / size) * 100,
    "mouth_5_rarity": (mouth5 / size) * 100,


    #   neck
    "neck_1_rarity": (neck1 / size) * 100,
    "neck_2_rarity": (neck2 / size) * 100,
    "neck_3_rarity": (neck3 / size) * 100,
    "neck_4_rarity": (neck4 / size) * 100,
    "neck_5_rarity": (neck5 / size) * 100,
 

    #   background

    "bg_1_rarity": (bg1 / size) * 100,
    "bg_2_rarity": (bg2 / size) * 100,
    "bg_3_rarity": (bg3 / size) * 100,
    "bg_4_rarity": (bg4 / size) * 100,
    "bg_5_rarity": (bg5 / size) * 100,


}

    #print(trait_dict)


total = 0

ranks = {}

back_rarity = 0
eyes_rarity = 0
head_rarity = 0
neck_rarity = 0
body_rarity = 0
acc_rarity = 0
mouth_rarity = 0
type_rarity = 0

for k in range(len(data)):

    print(data[k].get("metadata").get("name"))  # to get name
    traits = (data[k].get("metadata").get("attributes"))  # to get value
    count = 0

    for l in range(len(traits)): #find which combination of traits exist for each NFT
        #count must correspond with the order of the traits in the metadata, for traits with possiblity to roll 'None' value

        print(traits[l].get("value"))
        #   backgrounds
        if (traits[l]).get("value") == "bg1":
            back_rarity = trait_dict["bg_1_rarity"]
            count += 1
        elif (traits[l]).get("value") == "bg2":
            back_rarity = trait_dict["bg_2_rarity"]
            count += 1
        elif (traits[l]).get("value") == "bg3":
            back_rarity = trait_dict["bg3_rarity"]
            count += 1
        elif (traits[l]).get("value") == "bg4":
            back_rarity = trait_dict["bg_4_rarity"]
            count += 1
        elif (traits[l]).get("value") == "bg5":
            back_rarity = trait_dict["bg_5_rarity"]
            count += 1
        #   type
        elif (traits[l]).get("value") == "base1":
            type_rarity = trait_dict["base_1_rarity"]
            count += 1
        elif (traits[l]).get("value") == "base2":
            type_rarity = trait_dict["base_2_rarity"]
            count += 1
        elif (traits[l]).get("value") == "base3":
            type_rarity = trait_dict["base_3_rarity"]
            count += 1
        elif (traits[l]).get("value") == "base4":
            type_rarity = trait_dict["base_4_rarity"]
            count += 1
        elif (traits[l]).get("value") == "base5":
            type_rarity = trait_dict["base_5_rarity"]
            count += 1
            
        #   head
        elif (traits[l]).get("value") == "head1":
            head_rarity = trait_dict["head_1_rarity"]
            count += 1
        elif (traits[l]).get("value") == "head2":
            head_rarity = trait_dict["head_2_rarity"]
            count += 1
        elif (traits[l]).get("value") == "head3":
            head_rarity = trait_dict["head_3_rarity"]
            count += 1
        elif (traits[l]).get("value") == "head4":
            head_rarity = trait_dict["head_4_rarity"]
            count += 1
        elif (traits[l]).get("value") == "head5":
            head_rarity = trait_dict["head_5_rarity"]
            count += 1
        elif ((traits[l]).get("value") == "None") and (count == 2):
            head_rarity = trait_dict["no_head_rarity"]
            count += 1
            
        #   Neck
        elif (traits[l]).get("value") == "neck1":
            neck_rarity = trait_dict["neck_1_rarity"]
            count += 1
        elif (traits[l]).get("value") == "neck2":
            neck_rarity = trait_dict["neck_2_rarity"]
            count += 1
        elif (traits[l]).get("value") == "neck3":
            neck_rarity = trait_dict["neck_3_rarity"]
            count += 1
        elif (traits[l]).get("value") == "neck4":
            neck_rarity = trait_dict["neck_4_rarity"]
            count += 1
        elif (traits[l]).get("value") == "neck5":
            neck_rarity = trait_dict["neck_5_rarity"]
            count += 1
        elif ((traits[l]).get("value") == "None") and (count == 5):
            neck_rarity = trait_dict["no_neck_rarity"]
            count += 1
            
        #   eyes
        elif (traits[l]).get("value") == "eyes1":
            eyes_rarity = trait_dict["eyes_1_rarity"]
            count += 1
        elif (traits[l]).get("value") == "eyes2":
            eyes_rarity = trait_dict["eyes_2_rarity"]
            count += 1
        elif (traits[l]).get("value") == "eyes3":
            eyes_rarity = trait_dict["eyes_3_rarity"]
            count += 1
        elif (traits[l]).get("value") == "eyes4":
            eyes_rarity = trait_dict["eyes_4_rarity"]
            count += 1
        elif (traits[l]).get("value") == "eyes5":
            eyes_rarity = trait_dict["eyes_5_rarity"]
            count += 1
            
        #   body
        elif (traits[l]).get("value") == "body1":
            body_rarity = trait_dict["body_1_rarity"]
            count += 1
        elif (traits[l]).get("value") == "body2":
            body_rarity = trait_dict["body_2_rarity"]
            count += 1
        elif (traits[l]).get("value") == "body3":
            body_rarity = trait_dict["body_3_rarity"]
            count += 1
        elif (traits[l]).get("value") == "body4":
            body_rarity = trait_dict["body_4_rarity"]
            count += 1
        elif (traits[l]).get("value") == "body5":
            body_rarity = trait_dict["body_5_rarity"]
            count += 1
         elif ((traits[l]).get("value") == "None") and (count == 4):
            body_rarity = trait_dict["no_body_rarity"]
            count += 1
            
        #   accessory
        elif (traits[l]).get("value") == "acc1":
            acc_rarity = trait_dict["acc_1_rarity"]
            count += 1
        elif (traits[l]).get("value") == "acc2":
            acc_rarity = trait_dict["acc_2_rarity"]
            count += 1
        elif (traits[l]).get("value") == "acc3":
            acc_rarity = trait_dict["acc_3_rarity"]
            count += 1
        elif (traits[l]).get("value") == "acc4":
            acc_rarity = trait_dict["acc_4_rarity"]
            count += 1
        elif (traits[l]).get("value") == "acc5":
            acc_rarity = trait_dict["acc_5_rarity"]
            count += 1
        elif ((traits[l]).get("value") == "None") and (count == 6):
            acc_rarity = trait_dict["no_accessory_rarity"]
            count += 1
            
        #   mouth
        elif (traits[l]).get("value") == "mouth1":
            mouth_rarity = trait_dict["mouth_1_rarity"]
            count += 1
        elif (traits[l]).get("value") == "mouth2":
            mouth_rarity = trait_dict["mouth_2_rarity"]
            count += 1
        elif (traits[l]).get("value") == "mouth3":
            mouth_rarity = trait_dict["mouth_3_rarity"]
            count += 1
        elif (traits[l]).get("value") == "mouth4":
            mouth_rarity = trait_dict["mouth_4_rarity"]
            count += 1
        elif (traits[l]).get("value") == "mouth5":
            mouth_rarity = trait_dict["mouth_5_rarity"]
            count += 1
        elif ((traits[l]).get("value") == "None") and (count == 7):
            mouth_rarity = trait_dict["no_mouth_rarity"]
            count += 1
            
    #calculate total rarity
    ranks[data[k].get("metadata").get("name")] = (back_rarity * type_rarity * head_rarity * eyes_rarity * body_rarity *
                                                  neck_rarity * acc_rarity * mouth_rarity)

print(ranks)

sorted_values = sorted(ranks.values())  # Sort the values
sorted_ranks = {}

for m in sorted_values:
    for n in ranks.keys():
        if ranks[n] == m:
            sorted_ranks[n] = ranks[n]
            break

sorted_trait_values = sorted(trait_dict.values()) 
sorted_traits = {}

for o in sorted_trait_values:
    for p in trait_dict.keys():
        if trait_dict[p] == o:
            sorted_traits[p] = trait_dict[p]
            break
        
        #export data

with open('spreadsheet.csv', 'w') as outfile:
    writer = csv.DictWriter(outfile, ('ID#', 'Rank'))
    writer.writeheader()
    writer.writerow(ranks)


