#Arguement inputs Question
def stripandlowercase(question):
    #Response is stored with response variable; response is stripped and lowercased
    response = str(input(f"{question}\n>>> ")).strip().lower()
    #Returns the response
    return response

print(stripandlowercase("What's your name?"))