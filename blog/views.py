from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from .models import Project

# Create your views here.

all_theses =[
    
    {
        "slug":"drugs",
        "title": "Enhancing Drug Expenditure Forecasting in Belgium Using ARIMA and ETS Models on Incomplete Time Series Data",
        "content": 
        """
        
        <p>Healthcare expenditure is rising worldwide. The global average share of healthcare care expenditure increased from 4.6 %
        of the GDP in 1970 to 9.0 % in 2016. In Belgium, healthcare costs account for about 10% of the GPD, and the government is 
        the primary sponsor of the health system. Therefore, there is a growing interest among policymakers to foresee future
        costs so they can plan ahead. IMA (Inter Mutualist Agency) provided secondary data on the healthcare costs reimbursements.
        However, the data is not up to date. For now, complete data is available at the individual level from 2013 up to 2020,
        with an additional aggregate dataset available for 2021, although not complete. Hence, the present study has two main objectives:
        First, it aims to incorporate information on the incomplete part of the data into the model in the hope of improving forecasting.
        Second, it investigates whether increasing historical data will help improve the model</p>
                    
                    
         <p>The data is available at different frequency levels: a complete part of the data, which is available at monthly,
         quarterly, and yearly levels, and an incomplete part, which is available only at a yearly level.One could use only the complete part of the data to generate forecasts.
         In this case, some information would be ignored, which can be considered as a waste of information. 
         The goal is to combine both parts of the data under the same frequency level to generate forecasts.
         This study used a double forecast approach through ARIMA and ETS models to tackle this problem. 
         In the first step, we used ARIMA and ETS models on the complete part of the data to generate quarterly or monthly costs for one year.
         Then, the percentage of costs of each period (each quarter or each month) was used to disaggregate the annual cost. Once the annual data is disaggregated, 
         both parts of the data are combined to produce the final forecasts</p>
                    
         <p>To disaggregate the portion of the data that is incomplete and only available at the yearly level, we proceeded as follows:

First, we used the complete data to generate a one-year forecast at the desired frequency (monthly or quarterly). 
Then, we calculated the percentage of cost attributed to each period and used these percentages as proxies to disaggregate the annual data into quarterly or monthly data.

For example, to generate a quarterly forecast of drug costs for 2018, we used complete data up to 2016 and yearly data for 2017.
We first generated a quarterly forecast for 2017 using the complete data. Then, we calculated the percentage of total cost represented by
each quarter in the 2017 forecast. These percentages were used to disaggregate the 2017 annual cost into quarterly values.

Once the 2017 data was disaggregated, it was combined with the complete dataset to generate a forecast for 2018.
This process was repeated iteratively to generate forecasts for all subsequent years (see the figure below).</p>

<h4>Predictive modeling of drug costs</h4>

<img src='/static/images/z.png' alt='Forecasting illustration' style='max-width: 100%; height: auto;'/>

<p>
We compared two models: one that incorporates the incomplete portion of the data, and another that does not. 
The results showed that the model including the incomplete data produced better forecasts than the one that excluded it.

Furthermore, the results indicated that ARIMA outperformed ETS in predicting future drug costs within the context of this study,
as ARIMA consistently yielded smaller prediction errors.

Lastly, we compared three models based on different lengths of time series: the first used six years of data,
the second seven years, and the third eight years. This analysis aimed to address the second research question—whether
using a longer time series leads to improved forecast accuracy. However, the results were inconclusive. Therefore, 
a six-year time series appears sufficient for making reliable predictions using monthly or quarterly data.
</p>      
        """
    },
      
    {
        "slug":"trade",
        "title": "Does trade liberalisation counter food insecurity in Haiti",
        "content": 
        """
        
        
        
        <p>Despite tremendous strides in the fight against poverty across the globe during the last decades,
        food insecurity remains a significant concern worldwide, especially in developing countries. 
        The United Nations and other organizations such as WTO, WB, and IMF have elaborated policies to 
        offset this matter, yet the results are inconclusive. Trade liberalization is one of these policies 
        that aim to boost the world economy and challenge food insecurity globally.
        Although Haiti is one of the most open economies worldwide, the economic situation is alarming,
        where more than half of the population is highly food insecure. 
        This present study has two main objectives. First, it aims at investigating the 
        impact of trade liberalization on food security in Haiti. Second,
        it seeks to predict the effect of raising tariffs on sectorial outputs and food security if the country adopts protectionism.
        Secondary data were collected from the literature, and four types of scenarios
        were simulated through Computable General Equilibrium Modeling. Using the GAMS software for the simulations,
        the results reveal that trade liberalization improves food insecurity in Haiti.
        However, its adverse effects on the public deficits and the country's GDP make us believe that trade
        liberalization is beneficial only in the short run. Further trade liberalization would escalate the 
        volume of imports and increase the country's dependency on imports which would be detrimental in the long run.
        In addition, the results show that a protectionist stance would hurt consumers even more by raising the price of goods and services.
        Therefore, we suggest that the country continues to operate under free trade,
        but massive investment should be made to improve domestic production in order to counteract the long-run negative 
        effect of free trade. For further robustness checks,
        this study uses sensitivity analysis tests, and the findings are unaltered.!</p>
                    
                    
        
        """
    },  
    {
        "slug":"credit",
        "title": "Analysis of the impact of agricultural credit on farmers' income",
        "content": 
        """
        
        <p>It is clear that credit is an important and necessary tool for a country's economic development. Capital is generally 
        a limiting factor, and the use of external financing appears to be inevitable. However, FINCA Haiti S.A. has struggled to
        increase its agricultural credit client portfolio. This research aims to compare the per-hectare agricultural income of farms 
        that have benefited from agricultural credit with that of non-beneficiary farms,
        in order to highlight the importance of agricultural credit among beneficiaries and to identify the criteria that most
        influence credit demand, so that FINCA can expand its agricultural credit client base.

We start from the hypothesis that per-hectare agricultural incomes of beneficiaries are higher than those of non-beneficiaries,
and that the index of sociological criteria—including fear of commitment, negative testimonies about the institution’s agricultural credit,
administrative burdens, prevailing insecurity, and family influence—has a greater impact on credit demand than financial criteria,
which include interest rate, repayment capacity, collateral provision, loan amount granted, and market uncertainty.

This study was conducted in the 3rd and 4th sections of Petit Bois in the commune of Croix-des-Bouquets.
Two categories of agricultural holdings are found in each section: those benefiting from FINCA’s agricultural credit and those that are not.
The agricultural holding constitutes our statistical unit, and the size of the Utilized Agricultural Area (UAA) was used as a typology criterion.
Two types of holdings were distinguished within each category: farms with a UAA of less than one (1)
hectare and those with a UAA greater than or equal to one (1) hectare.

The results showed, on the one hand, that the average per-hectare agricultural incomes of beneficiary farms 
are higher than those of non-beneficiaries, averaging 203,095.65 HTG for FINCA Haiti S.A. beneficiaries compared to 159,510.8 HTG
for non-beneficiaries. On the other hand, that sociological criteria have a greater influence on credit demand than financial criteria,
with a total index of 284 for sociological criteria versus 211 for financial ones. The initial
hypotheses were tested and verified using the “T-Student” statistical test with IBM SPSS Statistics 23 and Excel 2016 software.</p>
                    
        
        """
    }
]

from datetime import date

all_projects = [
    {
        "title": "First-project",
        "slug": "first-project",
        "date" : date(2024,4,5),
        "content": 
            """
           This study was conducted in the 3rd and 4th sections of Petit Bois in the commune of Croix-des-Bouquets.
Two categories of agricultural holdings are found in each section: those benefiting from FINCA’s agricultural credit and those that are not.
The agricultural holding constitutes our statistical unit, and the size of the Utilized Agricultural Area (UAA) was used as a typology criterion.
Two types of holdings were distinguished within each category: farms with a UAA of less than one (1)
hectare and those with a UAA greater than or equal to one (1) hectare. 
            """
    },
    {
         "title": "Second-project",
        "slug": "first-project",
        "date" : date(2025,4,5),
        "content": 
            """
         The results showed, on the one hand, that the average per-hectare agricultural incomes of beneficiary farms 
are higher than those of non-beneficiaries, averaging 203,095.65 HTG for FINCA Haiti S.A. beneficiaries compared to 159,510.8 HTG
for non-beneficiaries. On the other hand, that sociological criteria have a greater influence on credit demand than financial criteria,
with a total index of 284 for sociological criteria versus 211 for financial ones. The initial
hypotheses were tested and verified using the “T-Student” statistical test with IBM SPSS Statistics 23 and Excel 2016 software.</p>
                    
            """
        
    },{
         "title": "Third-project",
        "slug": "Third-project",
        "date" : date(2025,4,5),
        "content": 
            """
         The results showed, on the one hand, that the average per-hectare agricultural incomes of beneficiary farms 
are higher than those of non-beneficiaries, averaging 203,095.65 HTG for FINCA Haiti S.A. beneficiaries compared to 159,510.8 HTG
for non-beneficiaries. On the other hand, that sociological criteria have a greater influence on credit demand than financial criteria,
with a total index of 284 for sociological criteria versus 211 for financial ones. The initial
hypotheses were tested and verified using the “T-Student” statistical test with IBM SPSS Statistics 23 and Excel 2016 software.</p>
                    
            """
        
    }
]



from django.views import View
from django.views.generic.base import TemplateView

from .forms import GeneralCommentForm  , CommentForm
from django.urls import reverse

def acceuil(request):
    return render(request, "blog/acceuil.html")


def theses(request):
    return render(request, "blog/theses.html")


def thesis_detail(request, slug):
    selected_thesis = next(thesis for thesis in all_theses if thesis["slug"]==slug)
    return render(request,"blog/thesis_details.html",{
       "thesis": selected_thesis 
    })



def projects(request):
    
    my_projects = Project.objects.all()
    
    return render(request, "blog/projects.html",{
        "projects": my_projects
    })


def project_detail(request, slug):
    selected_project1 = Project.objects.get(slug=slug)
    comment_form = CommentForm()
    # selected_project1 = next(project for project in all_projects if project["slug"]==slug)
    return render(request,"blog/project-details.html",{
        "project":selected_project1,
        "comment_form": comment_form
    })



def project_detail(request, slug):
   
    
    if request.method=="GET":
        project = Project.objects.get(slug=slug)
        comment_form = CommentForm()
        return render(request,"blog/project-details.html",{
        "project":project,
        "comment_form": comment_form,
        "comments": project.comments.all().order_by('-id')
         })
          
    else:
        comment_form = CommentForm(request.POST)
        project = Project.objects.get(slug=slug)
        
        if comment_form.is_valid():
            comment =comment_form.save(commit=False)
            comment.project= project
            comment.save()
            return HttpResponseRedirect(reverse("project_details", args=[slug]))
        else:
            return render(request,"blog/project-details.html",{
        "project":project,
        "comment_form": comment_form,
        "comments": project.comments.all().order_by('-id')
         })
            
        
        
        

  




def comment(request):
    
    
    if request.method =="GET":
        form = GeneralCommentForm()
            
    else:
        request_form = GeneralCommentForm(request.POST)
        if request_form.is_valid():
            request_form.save()
            return HttpResponseRedirect( "/thank_you")
            
        else:
            return render(request, "blog/general_comments.html",{
            "form":request_form
        })
            
    return render(request, "blog/general_comments.html",{
            "form":form
        })
            
            
            

            

def thank_you(request):
     return render(request, "blog/comment_suucess.html")
            
   
class thank_you1(TemplateView):
    template_name = "blog/comment_suucess.html"
    
        
        
       
        
    
from django.views.generic import DetailView    
        
class SingleProjectView(DetailView):
    
    template_name = "blog/project_details.html"
    model = Project

    