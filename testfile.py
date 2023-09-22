import json

def get_movable_item_ids(allqauters, moveable_items):
    all_quarter_item_ids = [item["item_id"] for quarter in allqauters for item in quarter["items"]]
    movable_item_ids = [item["item_id"] for item in moveable_items if item["item_id"] in all_quarter_item_ids]
    print(movable_item_ids)
    for quarter in allqauters:
        for item in quarter["items"]:
            if item["item_id"] in movable_item_ids:
                item["locked"] = True

    return allqauters

# JSON objects to compare
json_obj1 =  [{"quarter_label":"Fall-2022","quarter_num":1,"quarter_year":2022,"total_units":12,"items":[{"locked":False,"item_id":11,"code_name":"DS-301","letter":"Advanced Topics in Data Science","units":4,"predecessor":None,"simultaneous":None}, { "locked":False,"item_id":1,"code_name":"CSCI-201","letter":"Computer Systems Organization","units":4,"predecessor":None,"simultaneous":None},
         {
            "locked":False,
            "item_id":19,
            "code_name":"MEIS-104",
            "letter":"Foreign Language",
            "units":4,
            "predecessor":None,
            "simultaneous":None
         }
      ]
   },
   {
      "quarter_label":"Spring-2023",
      "quarter_num":2,
      "quarter_year":2023,
      "total_units":16,
      "items":[
         {
            "locked":False,
            "item_id":14,
            "code_name":"MATH-235",
            "letter":"Probability and Statistics",
            "units":4,
            "predecessor":None,
            "simultaneous":None
         },
         {
            "locked":False,
            "item_id":18,
            "code_name":"CORE-126",
            "letter":"Expressive Culture",
            "units":4,
            "predecessor":None,
            "simultaneous":None
         },
         {
            "locked":False,
            "item_id":10,
            "code_name":"DS-202",
            "letter":"Responsible Data Science",
            "units":4,
            "predecessor":None,
            "simultaneous":None
         },
         {
            "locked":False,
            "item_id":2,
            "code_name":"CSCI-202",
            "letter":"Operating Systems",
            "units":4,
            "predecessor":None,
            "simultaneous":None
         }
      ]
   },
   {
      "quarter_label":"Fall-2023",
      "quarter_num":1,
      "quarter_year":2023,
      "total_units":20,
      "items":[
         {
            "locked":False,
            "item_id":15,
            "code_name":"CORE-123",
            "letter":"Quantitative Reasoning",
            "units":4,
            "predecessor":None,
            "simultaneous":None
         },
         {
            "locked":False,
            "item_id":4,
            "code_name":"CSCI-475",
            "letter":"Predictive Analytics",
            "units":4,
            "predecessor":None,
            "simultaneous":None
         },
         {
            "locked":False,
            "item_id":13,
            "code_name":"MATH-140",
            "letter":"Linear Algebra",
            "units":4,
            "predecessor":None,
            "simultaneous":None
         },
         {
            "locked":False,
            "item_id":5,
            "code_name":"CSCI-473",
            "letter":"Intro to Machine Learning",
            "units":4,
            "predecessor":None,
            "simultaneous":None
         },
         {
            "locked":False,
            "item_id":6,
            "code_name":"CSCI-479",
            "letter":"Data Management and Analysis",
            "units":4,
            "predecessor":None,
            "simultaneous":None
         }
      ]
   },
   {
      "quarter_label":"Spring-2024",
      "quarter_num":2,
      "quarter_year":2024,
      "total_units":16,
      "items":[
         {
            "locked":False,
            "item_id":12,
            "code_name":"MATH-122",
            "letter":"Calculus II",
            "units":4,
            "predecessor":None,
            "simultaneous":None
         },
         {
            "locked":False,
            "item_id":17,
            "code_name":"CORE-125",
            "letter":"Societies & Social Sciences",
            "units":4,
            "predecessor":None,
            "simultaneous":None
         },
         {
            "locked":False,
            "item_id":8,
            "code_name":"DS-112",
            "letter":"Introduction to Data Science",
            "units":4,
            "predecessor":None,
            "simultaneous":None
         },
         {
            "locked":False,
            "item_id":3,
            "code_name":"CSCI-310",
            "letter":"Basic Algorithms",
            "units":4,
            "predecessor":None,
            "simultaneous":None
         }
      ]
   },
   {
      "quarter_label":"Fall-2024",
      "quarter_num":1,
      "quarter_year":2024,
      "total_units":12,
      "items":[
         {
            "locked":False,
            "item_id":7,
            "code_name":"DS-111",
            "letter":"Data Science for Everyone",
            "units":4,
            "predecessor":None,
            "simultaneous":None
         },
         {
            "locked":False,
            "item_id":16,
            "code_name":"CORE-124",
            "letter":"Cultures and Contexts",
            "units":4,
            "predecessor":None,
            "simultaneous":None
         },
         {
            "locked":False,
            "item_id":9,
            "code_name":"DS-201",
            "letter":"Causal Inference",
            "units":4,
            "predecessor":None,
            "simultaneous":None
         }
      ]
   }
]
json_obj2 = [{"locked":False,"item_id":2,"code_name":"CSCI-202","letter":"Operating Systems", "units":4, "predecessor":None,"simultaneous":None  },{ "locked":False, "item_id":15, "code_name":"CORE-123","letter":"Quantitative Reasoning","units":4,"predecessor":None,"simultaneous":None}]

# Call the function to check if the JSON objects are the same
result = get_movable_item_ids(json_obj1, json_obj2)
# print(result)

# for quater in json_obj1:
#     print(quater)
    # for item in quater["items"]:
    #     print(item["item_id"])

