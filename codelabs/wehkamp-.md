authors: Sparsh A.
categories: Story
feedback link: https://github.com/recohut/reco-step/issues
id: wehkamp
status: Published
summary: Dutch retailer Wehkamp offers their shoppers a wide range of quality products. They carry the latest fashion trends, home-goods, electronics and everything in between. As a leading e-commerce company in fashion in the Netherlands, they dedicates itself to provide a better shopping experience for the customers, and continually looks for ways to not only engage shoppers on their site, but also create opportunities for their brand partners to clearly demonstrate their value. Their main marketing focus is relevance — ensuring their shoppers are able to find what they need in the most efficient way. This puts shoppers in a purchasing frame of mind when they visit Wehkamp’s website.

---

# Wehkamp

<!-- ------------------------ -->

## Introduction

Duration: 5

![img/_markdowns-raw-recostep-stage-wehkamp-untitled.png](img/_markdowns-raw-recostep-stage-wehkamp-untitled.png)

Dutch retailer Wehkamp offers their shoppers a wide range of quality products. They carry the latest fashion trends, home-goods, electronics and everything in between. As a leading e-commerce company in fashion in the Netherlands, they dedicates itself to provide a better shopping experience for the customers, and continually looks for ways to not only engage shoppers on their site, but also create opportunities for their brand partners to clearly demonstrate their value. Their main marketing focus is relevance — ensuring their shoppers are able to find what they need in the most efficient way. This puts shoppers in a purchasing frame of mind when they visit Wehkamp’s website.

### History

![img/_markdowns-raw-recostep-stage-wehkamp-untitled-1.png](img/_markdowns-raw-recostep-stage-wehkamp-untitled-1.png)

### Company statistics

![img/_markdowns-raw-recostep-stage-wehkamp-untitled-2.png](img/_markdowns-raw-recostep-stage-wehkamp-untitled-2.png)

### Machine learning at Wehkamp

![img/_markdowns-raw-recostep-stage-wehkamp-untitled-3.png](img/_markdowns-raw-recostep-stage-wehkamp-untitled-3.png)

### Key features of the recommender system

- Fully managed platform on AWS: Automated cluster management simplifies the infrastructure and operations at any scale.
- More efficient data flow: Able to easily integrate with other tools like airflow and Kubernetes, allowing them to build automated data pipelines while establishing CI/CD best practices.
- Improved cross-team collaboration: Collaborative notebook environment with support for multiple languages (SQL, Scala, Python, R) enables a diverse team of users to work together in their preferred language allowed them to accelerate data science operations and innovation.
- Streamlined ML lifecycle: Native support for MLflow enables data science teams to easily replicate experiments, track model performance, and rapidly iterate across their models in a systematic fashion.

### Tech stack

![img/_markdowns-raw-recostep-stage-wehkamp-untitled-4.png](img/_markdowns-raw-recostep-stage-wehkamp-untitled-4.png)

<!---------------------------->

## Ranking problem

Duration: 5

A major topic for the data science team is ranking products. If a visitor enters a search phrase, what are the best products that fit the search phrase and in what order should the products been shown? Ranking products is also important if a visitor enters a product overview page, where hundreds or even thousands of products of a certain article type are displayed.

For instance, when a user search for 'jeans' on wehkamp website, it returns 4400+ products. User navigates to 'ladies jeans' overview page. The search result page now has 2176 products. So the goal is to maximize the order of relevance of returned products given a user query. 

![img/_markdowns-raw-recostep-stage-wehkamp-untitled-5.png](img/_markdowns-raw-recostep-stage-wehkamp-untitled-5.png)

![img/_markdowns-raw-recostep-stage-wehkamp-untitled-6.png](img/_markdowns-raw-recostep-stage-wehkamp-untitled-6.png)

![img/_markdowns-raw-recostep-stage-wehkamp-untitled-7.png](img/_markdowns-raw-recostep-stage-wehkamp-untitled-7.png)

![img/_markdowns-raw-recostep-stage-wehkamp-untitled-8.png](img/_markdowns-raw-recostep-stage-wehkamp-untitled-8.png)

<!---------------------------->

## Data collection

Duration: 2

![img/_markdowns-raw-recostep-stage-wehkamp-untitled-9.png](img/_markdowns-raw-recostep-stage-wehkamp-untitled-9.png)

<!---------------------------->

## Click model

Duration: 5

![img/_markdowns-raw-recostep-stage-wehkamp-untitled-10.png](img/_markdowns-raw-recostep-stage-wehkamp-untitled-10.png)

![img/_markdowns-raw-recostep-stage-wehkamp-untitled-11.png](img/_markdowns-raw-recostep-stage-wehkamp-untitled-11.png)

![img/_markdowns-raw-recostep-stage-wehkamp-untitled-12.png](img/_markdowns-raw-recostep-stage-wehkamp-untitled-12.png)

<!---------------------------->

## Feature generation

Duration: 2

![img/_markdowns-raw-recostep-stage-wehkamp-untitled-13.png](img/_markdowns-raw-recostep-stage-wehkamp-untitled-13.png)

![img/_markdowns-raw-recostep-stage-wehkamp-untitled-14.png](img/_markdowns-raw-recostep-stage-wehkamp-untitled-14.png)

![img/_markdowns-raw-recostep-stage-wehkamp-untitled-15.png](img/_markdowns-raw-recostep-stage-wehkamp-untitled-15.png)

![img/_markdowns-raw-recostep-stage-wehkamp-untitled-16.png](img/_markdowns-raw-recostep-stage-wehkamp-untitled-16.png)

<!---------------------------->

## Ranking model

Duration: 5

Notebook jobs were used to process raw data and generate features. XGBoost model was trained on these features. HyperOpt and MLflow were used for hyperparameter optimization and experiment tracking respectively. For identifying feature importances and explaining them, SHAP was used. 

![img/_markdowns-raw-recostep-stage-wehkamp-untitled-17.png](img/_markdowns-raw-recostep-stage-wehkamp-untitled-17.png)

![img/_markdowns-raw-recostep-stage-wehkamp-untitled-18.png](img/_markdowns-raw-recostep-stage-wehkamp-untitled-18.png)

![img/_markdowns-raw-recostep-stage-wehkamp-untitled-19.png](img/_markdowns-raw-recostep-stage-wehkamp-untitled-19.png)

<!---------------------------->

## Serve model

Duration: 5

Model was saved in Elastic index. 

![img/_markdowns-raw-recostep-stage-wehkamp-untitled-20.png](img/_markdowns-raw-recostep-stage-wehkamp-untitled-20.png)

![img/_markdowns-raw-recostep-stage-wehkamp-untitled-21.png](img/_markdowns-raw-recostep-stage-wehkamp-untitled-21.png)

<!---------------------------->

## Evaluation

Duration: 5

![img/_markdowns-raw-recostep-stage-wehkamp-untitled-22.png](img/_markdowns-raw-recostep-stage-wehkamp-untitled-22.png)

![img/_markdowns-raw-recostep-stage-wehkamp-untitled-23.png](img/_markdowns-raw-recostep-stage-wehkamp-untitled-23.png)

<!---------------------------->

## Conclusion

Duration: 2

Congratulations!

### Links and References

1. [https://youtu.be/6BGCn3h59nA](https://youtu.be/6BGCn3h59nA)
2. [Applied Machine Learning for Ranking Products in an Ecommerce Setting](https://databricks.com/session_eu19/applied-machine-learning-for-ranking-products-in-an-ecommerce-setting)

### Have a Question?

- [Fill out this form](https://form.jotform.com/211377288388469)
- [Raise issue on Github](https://github.com/recohut/reco-step/issues)