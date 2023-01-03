from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings
import os
import PyPDF2
import re
import string



# Create your views here.
def index(request):
    context = {}
    template = loader.get_template('analytics/index.html')
    return HttpResponse(template.render(context, request))


def sample_analytics(request):
    context = {}
    sample_brainmap = open(os.path.join(settings.STATICFILES_DIRS[0], 'pdf/BrainmapSampleReport.pdf'), 'rb')
    pdf_reader = PyPDF2.PdfFileReader(sample_brainmap)
    pages = pdf_reader.numPages
    context['pages'] = []
    for i in range(0, pages):
        page = pdf_reader.getPage(i)
        text = page.extract_text()
        lines = text.replace("\r", "").split("\n")
        #record = {}
        if i == 0:
            try:
                start = lines.index("Client Name:")
                name = lines[start + 1]
                num = lines.index("Client Number:")
                client_num = lines[num + 1]
                date = lines.index("Map Date:")
                map_date = lines[date + 1]
                context['client_name'] = name
                context['client_number'] = client_num
                context['map_date'] = map_date
            except:
                raise Exception("No Client Information Found")
        if "Suggested Supplements" not in text:
            continue
        for i, line in enumerate(lines):
            tabs = line.split("\t")
            if tabs:
                line = "|".join(tabs)
            vtabs = line.split("\x0b")
            if vtabs:
                line = "~~~".join(vtabs)
            lines[i] = line
        context['supplements'] = []
        try:
            sug_sups = lines.index("Suggested Supplements")
            sups = []
            idx = sug_sups + 2

            while "Client Name:" not in lines[idx]:
                sups.append(lines[idx])
                idx += 1
            last_sup = lines[idx]
            cidx = last_sup.find("Client Name:")
            sups.append(last_sup[0:cidx])
            context['supplements'] = sups
        except:
            raise Exception("No Supplements Section found.")
        # ws = string.whitespace
        # ws = ws[1:]
        # phrases = re.split(ws, text)
        # print(phrases)
            context['pages'].append(line)

        # for phrase in phrases:
        #     phrase.strip()
        #     print(phrase)
        # idx = -1
        # try:
        #     idx = phrases.index("Suggested")
        #     print(phrases[idx:])
        # except:
        #     pass

        #for image in page.images:
        #    context['pages'].append(image.name)
        #context['pages'].append(page.extractText())
        #context['pages'].extend(page.extractText().split())
    sample_brainmap.close()
    # sample_neuro = open(os.path.join(settings.STATICFILES_DIRS[0], 'pdf/NeurotransmitterSampleReport.pdf'), 'rb')
    # pdf_reader = PyPDF2.PdfFileReader(sample_neuro)
    # pages = pdf_reader.numPages
    # context['npages'] = []
    # for i in range(0, pages):
    #     page = pdf_reader.getPage(i)
    #     context['npages'].append(page.extractText())
    #     context['npages'].extend(page.extractText().split())
    # sample_neuro.close()
    template = loader.get_template('analytics/sample_analytics.html')
    return HttpResponse(template.render(context, request))
