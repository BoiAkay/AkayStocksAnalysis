import pandas as pd
from commonModuleImport import *

bootstrap_classes = """<table class="table table-striped table-bordered">"""
def generateHTML(timePeriod):

    
    if(timePeriod=="1mo"):
        csv_file_path = "data/STOCKS_RETURN_1mon.csv"
        htmlFilePath = "data/Return1mon.html"
    if(timePeriod=="1y"):
        csv_file_path = "data/STOCKS_RETURN_1YR.csv"
        htmlFilePath = "data/Return1YR.html"

    df = pd.read_csv(csv_file_path)
    # html_table = df.to_html(index=False, classes=bootstrap_classes)
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>{timePeriod} Return's Data</title>
    </head>
    <body>
    <h1>{timePeriod} Return</h1>
    {df.to_html(index=False, classes=bootstrap_classes)}
    </body>
    </html>
    """
    # Write the HTML code to a file
    with open(htmlFilePath, "w") as f:
        f.write(html_code)

    print(f"HTML table successfully created: data.html")
    print(Akaycolours.BOLD+Akaycolours.BLUE+f'HTML created for {timePeriod} returns')
