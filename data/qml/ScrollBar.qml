// import QtQuick 1.0 // to target S60 5th Edition or Maemo 5
import QtQuick 1.1

Rectangle {
    property variant flickable

    id: scrollBar
    smooth: true
    radius: width / 2
    color: "#28ffffff"

    Rectangle {
        id: handle
        width: scrollBar.width + 1
        height: flickable.visibleArea.heightRatio * (scrollBar.height)
        x: -1
        y: flickable.visibleArea.yPosition * (scrollBar.height - 2)
        smooth: true
        color: "#1a1a1a"
        radius: width / 2
        border.width: 1
        border.color: "#36ffffff"

        MouseArea {
            anchors.fill: parent
            drag.target: handle
            drag.axis: Drag.YAxis
            drag.minimumY: 0
            drag.maximumY: scrollBar.height - handle.height

            onPositionChanged: {
                flickable.contentY = handle.y * flickable.contentHeight / scrollBar.height
            }
        }
    }
}
