# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def get_hash(x):
    return (2*x+3)%1000003%1000

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    hashTable = [[] for i in range(1000)]
    # Keep list of all existing (i.e. not deleted yet) contacts.
    #contacts = []
    for cur_query in queries:
        hashValue = get_hash(cur_query.number)
        if cur_query.type == 'add':
            
            for x in hashTable[hashValue]:
                if x.number == cur_query.number:
                    x.name = cur_query.name
                    break
            else:
                    hashTable[hashValue].append(cur_query)
            # if we already have contact with such number,
            # we should rewrite contact's name
            #for contact in contacts:
             #   if contact.number == cur_query.number:
              #      contact.name = cur_query.name
               #     break
            #else: # otherwise, just add it
             #   contacts.append(cur_query)
        elif cur_query.type == 'del':
            '''
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
            '''
            for x in hashTable[hashValue]:
                if x.number == cur_query.number:
                    hashTable[hashValue].remove(x)
                    break
        else:
            response = 'not found'
            for x in hashTable[hashValue]:
                if x.number == cur_query.number:
                    response = x.name
                    break
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

