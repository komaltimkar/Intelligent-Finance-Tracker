
from .models import Transaction, SavingsGoal
from django.http import JsonResponse
from django.shortcuts import render, redirect
from reportlab.lib.pagesizes import letter

# Dashboard View (This should return a dashboard page)
from django.http import HttpResponse
from io import BytesIO
from reportlab.pdfgen import canvas

# Logout View  # Redirect to login page after logging out
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm, ExpenseForm
from django.contrib.auth import authenticate, login
# Registration View
# views.py
from django.contrib import messages


from django.contrib.auth.decorators import login_required
def home(request):
    return render(request,'home.html')
@login_required

def dashboard(request):
    return render(request, 'dashboard.html')  # Assuming you have a dashboard.html template

def dashboard(request):
    if request.user.is_authenticated:
        # Fetch transactions for the logged-in user
        transactions = Transaction.objects.filter(user=request.user).order_by('-created_at')
        total_income = sum(t.amount for t in transactions if t.type == 'Income')
        total_expense = sum(t.amount for t in transactions if t.type == 'Expense')
        remaining_balance = total_income - total_expense
        
        context = {
            'transactions': transactions,
            'total_income': total_income,
            'total_expense': total_expense,
            'remaining_balance': remaining_balance,
        }
        return render(request, 'dashboard.html', context)
    else:
        return redirect('login') 
    
    '''transactions = Transaction.objects.all()
    total_income = sum(t.amount for t in transactions if t.type == 'Income')
    total_expense = sum(t.amount for t in transactions if t.type == 'Expense')
    remaining_balance = total_income - total_expense

    try:
        savings_goal = SavingsGoal.objects.first()
    except SavingsGoal.DoesNotExist:
        savings_goal = None

    context = {
        'total_income': total_income,
        'total_expense': total_expense,
        'remaining_balance': remaining_balance,
        'savings_goal': savings_goal
    }
    return render(request, 'dashboard.html', context)'''
@login_required
def add_expense(request):
    # Add expense functionality here
    pass

@login_required
def expense_list(request):
    # Expense listing functionality here
    pass

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("successfully registered")
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to expense list page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('login')
def download_pdf(request):
    if request.user.is_authenticated:
        transactions = Transaction.objects.filter(user=request.user).order_by('-created_at')
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="transactions.pdf"'
        
        # Generate the PDF
        p = canvas.Canvas(response)
        p.drawString(100, 800, "Date\t\tDescription\t\tAmount\t\tType")
        y = 780  # Initial y-coordinate

        for transaction in transactions:
            row = f"{transaction.created_at}\t{transaction.description}\t{transaction.amount}\t{transaction.type}"
            p.drawString(100, y, row)
            y -= 20  # Move to the next line

        p.showPage()
        p.save()
        return response
    else:
        return redirect('login') 
#transactions = Transaction.objects.filter(user=request.user).order_by('-created_at')
  # Debugging to check if data is retrieved

#for transaction in transactions:
        #print(transaction.created_at, transaction.description, transaction.amount, transaction.type)
@login_required
def expenses(request):
    user_expenses = Transaction.objects.filter(user=request.user).order_by('-date')
    return render(request, 'templates/dashboard.html', {'expenses': user_expenses})
def add_transaction(request):
    if request.method == "POST":
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        type= request.POST.get('type')
        user = request.user

        # Save to the database
        transaction = Transaction.objects.create(
            user=user,
            amount=amount,
            description=description,
            type=type
        )
        transaction.save()
        return redirect('home')

    return render(request, 'add_transaction.html')
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, 'Expense added successfully!')
            return redirect('expenses')
    else:
        form = ExpenseForm()

    return render(request, 'templates/dashboard.html', {'form': form})
    if request.method == 'POST':
        type = request.POST.get('type')
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        
        # Ensure the user is assigned
        Transaction.objects.create(
            user=request.user,  # This must be set to the logged-in user
            type=type,
            description=description,
            amount=amount
        )
        return redirect('dashboard')

        return JsonResponse({'status': 'success'})
@login_required
def delete_transaction(request, transaction_id):
    try:
        transaction = Transaction.objects.get(id=transaction_id,user=request.user)
        transaction.delete()
        return JsonResponse({'status': 'success'})
    except Transaction.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Transaction not found'})

def set_savings_goal(request):
    if request.method == 'POST':
        goal_amount = float(request.POST['goal_amount'])
        savings_goal, created = SavingsGoal.objects.update_or_create(
            id=1, defaults={'goal_amount': goal_amount}
        )
        return JsonResponse({'status': 'success', 'goal_amount': savings_goal.goal_amount})
