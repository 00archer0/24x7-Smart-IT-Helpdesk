from django.shortcuts import render
from .helpdesk import Smart_IT_Helpdesk_ as hl
# Create your views here.



class q:
    Ques = ''
    counter = 0
    index = -1
    
const = q() 
 

    
# Create your views here.
# first page
def index(request):
    
    return render(request,'chatbot/Index.html')

#view function for response to clinet query
def querySubmission(request):
    if request.method == 'POST':        
        Query = request.POST['question']
        if Query == '':
            context = {'query':"Don't you have any question?"}
            return render(request,'chatbot/addAnswer.html',context)
        print(Query)
        Response,const.index = hl.get_response(Query)
        if Response[0] == "Model have to learn more vocabulary, Lack of Data or check your vocabulary":
            const.Ques   = Query
        print(Response)
        context = {'query':Query,
                "text":Response[0],
                "itemlist":Response,
                }    
    return render(request,'chatbot/answer_template.html',context)

# to add new question answer to database
def queryAddition(request):
    if request.method == 'POST':        
        Query = request.POST['input']
        context = {'query':Query}    
    return render(request,'chatbot/addAnswer.html',context)


def sub_ans(request):
    if request.method == 'POST':        
        ans = request.POST['input']
        hl.quesToDatabase(const.Ques,ans)
        if const.counter <10:
            const.counter +=1            
            context = {'query':'Model will be update after '+ str(10 - const.counter) + ' more contributions',
                       'status':'no'}
        else:
            const.counter = 0
            context = {'query':'Updated',
                       'status':'yes'}
    
    return render(request,'chatbot/addAnswer.html',context)

## to feedback function
def feedback(request):
    if request.method == 'POST':        
        ans = request.POST['value']
        hl.feedback(ans,const.index)
        print(ans)
        
    return render(request,'chatbot/addAnswer.html')

def save_changes(request):
    if request.method == 'POST':    
        hl.save_changes()
    return render(request,'chatbot/addAnswer.html')
    