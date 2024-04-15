class AppJavaScriptLoader():
    def __init__(self) -> None:
        self.jslist = []

    def addjscode(self,js: str):
        self.jslist.append(f"""
        <script language="javascript">
        {js}
        </script>
        """)

    def addjsfile(self,jsfile: str):
        with open(jsfile,'r') as f:
            jscode = f.read()
            self.jslist.append(f"""
            <script language="javascript">
            {jscode}
            </script>
            """)

    def __str__(self) -> str:
        return """
<html>
    <head>
        <title>AppJavaScriptLoader</title>
        {}
    </head>
    <body>
    </body>
</html>
        """.format("\n".join(self.jslist))
