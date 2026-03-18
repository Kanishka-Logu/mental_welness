from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import JournalEntry
from .forms import JournalEntryForm

@login_required
def journal_list(request):
    entries = JournalEntry.objects.filter(user=request.user)
    return render(request, 'journal/list.html', {'entries': entries})

@login_required
def journal_create(request):
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('journal_detail', pk=entry.pk)
    else:
        form = JournalEntryForm()
    return render(request, 'journal/form.html', {'form': form, 'title': 'Create Journal Entry'})

@login_required
def journal_detail(request, pk):
    entry = get_object_or_404(JournalEntry, pk=pk, user=request.user)
    return render(request, 'journal/detail.html', {'entry': entry})

@login_required
def journal_update(request, pk):
    entry = get_object_or_404(JournalEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        form = JournalEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('journal_detail', pk=entry.pk)
    else:
        form = JournalEntryForm(instance=entry)
    return render(request, 'journal/form.html', {'form': form, 'title': 'Update Journal Entry'})

@login_required
def journal_delete(request, pk):
    entry = get_object_or_404(JournalEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        entry.delete()
        return redirect('journal_list')
    return render(request, 'journal/confirm_delete.html', {'entry': entry})
