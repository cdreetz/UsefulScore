from pymongo import MongoClient
import certifi

def print_job_post_stats():
    # Connect to MongoDB server
    uri = "mongodb+srv://cdreetz:MszRQ839uVZhT0WG@cluster0.hxuskkk.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, tlsCAFile=certifi.where())

    # Select database and collection
    db = client['Cluster0']
    jobs_collection = db['jobs']

    # Count the total number of documents in the collection
    num_documents = jobs_collection.count_documents({})

    example_document = jobs_collection.find_one({})
    fields = list(example_document.keys())

    unique_roles = jobs_collection.distinct("role")
    num_roles = len(unique_roles)

    unique_companies = jobs_collection.distinct("company")
    num_companies = len(unique_companies)


    return num_documents
    #print(f'The total number of job posts we have collected data from is: {num_documents}')
    #print("The fields collected for each post are:", fields)
    #print("The total number of unique job roles:", num_roles)
    #print("The number of companies that these jobs come from:", num_companies)
    #print("Below is how many of each of those job roles we collected:")
    #for role in unique_roles:
        #count = jobs_collection.count_documents({"role": role})
        #print(role, ":", count)
