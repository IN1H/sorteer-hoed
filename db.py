from dotenv.main import dotenv_values
from supabase import create_client, Client

class Database:

    # Laad de supabase sleutel en url.
    config = dotenv_values(".env")

    # Maak de supabase client met onze sleutel en url
    supabase: Client = create_client(
        config["SUPABASE_URL"], 
        config["SUPABASE_KEY"]
    )

    def get_all(self):
        return (self.supabase.table('Vragen').select('id, question, Answers(answer, FICT, SE, IAT, BDAM, niks)').execute())["data"]

    def get_questions(self):
        arr =[]
        for vraag in (self.supabase.table('Vragen').select('id, question, Answers(answer, FICT, SE, IAT, BDAM, niks)').execute())["data"]:
            arr.append(vraag["question"])

        return arr

    def get_answers(self):
        arr=[]

        for vraag in self.get_all():
            temp =[]
            for antwoorden in vraag["Answers"]:
                temp.append(antwoorden["answer"])
            
            arr.append(temp)
        
        return arr

    def get_answer_by_id(self, id):
        return (self.supabase.table('Answers').eq("id", f"{id}").execute())["data"]

Database().get_questions()