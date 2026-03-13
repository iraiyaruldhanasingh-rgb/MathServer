from django.shortcuts import render

def calculate_bill(request):
    bill = 0

    if request.method == 'POST':
        p = float(request.POST.get('Price', 0))
        gst = float(request.POST.get('GST', 0))
        bill = p + (p * gst / 100)

        print("Price =", p)
        print("GST =", gst)
        print("Total Bill =", bill)

    return render(request, 'myapp/myapp.html', {'bill': bill})