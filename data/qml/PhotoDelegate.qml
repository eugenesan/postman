import QtQuick 1.1

Package {
    Item { id: gridItem; Package.name: 'gridPart'; width: 240; height: 240; z: 1 }
    Item { id: pathItem; Package.name: 'stackPart'; width: 240; height: 240; visible: PathView.onPath }

    Item {
        anchors.fill: parent

        Item {
            id: photoWrapper
            x: 0
            y: 0
            width: 190
            height: 190

            property double stackRotation: Math.random() * 24 - 12

            BorderImage {
                anchors {
                    leftMargin: -6; topMargin: -6; rightMargin: -8; bottomMargin: -8
                    fill: placeholder
                }
                source: "images/boxShadow.png"
                smooth: true
                border.left: 10; border.top: 10
                border.right: 10; border.bottom: 10
            }

            Rectangle {
                id: placeholder
                color: "#ffffff"
                smooth: true
                width: imageView.paintedWidth + 6
                height: imageView.paintedHeight + 6
                anchors.centerIn: parent
                Rectangle {
                     color: "#878787"; smooth: true
                     anchors { fill: parent; topMargin: 3; bottomMargin: 3; leftMargin: 3; rightMargin: 3 }
                }
            }

            Image {
                id: imageView
                source: filePath
                anchors.fill: parent
                clip: true
                fillMode: Image.PreserveAspectFit
                sourceSize.width: 300
            }

            MouseArea {
                anchors.fill: parent
                onClicked: {
                    if (postcardViewer.state == 'stackView')
                        postcardViewer.state = 'gridView'
                    else if (postcardViewer.state == 'gridView') {
                        gridPhotoView.currentIndex = index
                        //postcardViewer.state = 'stackView'
                    }
                }
            }

            Rectangle {
                id: destroyButton
                width: 20
                height: 20
                anchors.right: imageView.right
                anchors.top: imageView.top
                anchors.rightMargin: ((imageView.width - imageView.paintedWidth) / 2) - (width / 2)
                anchors.topMargin: ((imageView.height - imageView.paintedHeight) / 2) - (height / 2)
                color: "#000000"
                radius: width / 2
                border.width: 2
                border.color: "#ffffff"
                scale: photoWrapper.state == 'inGrid' ? 1.0 : 0.0

                Behavior on scale {
                    NumberAnimation { duration: 400 }
                }

                Image {
                    anchors.fill: parent
                    anchors.margins: 5
                    smooth: true
                    source: "images/closeSymbol.png"
                }

                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        shrinkAnimation.start()
                        destructionTimer.start()
                    }
                }
            }

            PropertyAnimation { id: shrinkAnimation; target: photoWrapper; property: 'scale'; to: 0; duration: 300; easing.type: Easing.InOutBack }

            Timer {
                id: destructionTimer; interval: 300; repeat: false
                onTriggered: {
                    imageListModel.remove(index)

                    if (imageListModel.count() === 0)
                        postcardViewer.state = 'stackView'
                }
            }

            states: [
                State {
                    name: 'inGrid'
                    ParentChange { target: photoWrapper; parent: gridItem; x: 25; y: 25 }
                    when: postcardViewer.state === 'gridView'
                },
                State {
                    name: 'inStack'
                    ParentChange { target: photoWrapper; parent: pathItem; x: 25; y: 25 }
                    PropertyChanges { target: photoWrapper; rotation: photoWrapper.stackRotation }
                    when: postcardViewer.state === 'stackView'
                }
            ]

            transitions: [
                Transition {
                    from: 'inStack,inGrid'
                    to: 'inGrid,inStack'
                    ParentAnimation {
                        target: photoWrapper
                        NumberAnimation { properties: 'x,y'; duration: 400; easing.type: Easing.InOutQuad }
                    }
                    PropertyAnimation { target: photoWrapper; property: 'rotation'; duration: 400; easing.type: Easing.OutQuad }
                }
            ]
        }
    }
}
