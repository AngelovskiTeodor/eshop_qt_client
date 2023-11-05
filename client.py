import sys
import requests
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

QML = """
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {{
    height: 320
    width: 480
    visible: true
    title: "E-Shop"

    readonly property list<string> titles: {}
    readonly property list<string> prices: {}

    function changeProduct() {{
        var i = Math.round(Math.random() * 3)
        title.text = titles[i]
        price.text = prices[i]
    }}

    ColumnLayout {{
        anchors.fill:  parent

        Text {{
            id: title
            text: "Product title"
            font.pixelSize: 18
            Layout.alignment: Qt.AlignHCenter
        }}
        Text {{
            id: price
            text: "Product price"
            Layout.alignment: Qt.AlignHCenter
        }}
        Button {{
            text: "Next product"
            Layout.alignment: Qt.AlignHCenter
            onClicked:  changeProduct()
        }}
    }}
}}
"""

if __name__=="__main__":
    eshop_api = "https://shagged-destroyers.000webhostapp.com/public/index.php/api"
    response = requests.get(eshop_api)

    titles = []
    prices = []
    for product in response.json():
        titles.append(product["name"])
        prices.append(product["price"])
    QML = QML.format(titles, prices)

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.loadData(QML.encode('utf-8'))

    if not engine.rootObjects():
        sys.exit(-1)
    exit_code = app.exec()
    del engine
    sys.exit(exit_code)