// import QtQuick 1.0 // to target S60 5th Edition or Maemo 5
import QtQuick 1.1

Flipable {
    property bool flipped: false

    id: envelope
    height: width * 0.66
    rotation: Math.random() - 0.5 * 6

    front: EnvelopeFront { }
    back: EnvelopeBack { }

    transform: Rotation {
        id: flipRotation
        origin.x: envelope.width / 2
        origin.y: envelope.height / 2
        axis.x: 0; axis.y: 1; axis.z: 0
    }

    states: State {
        name: "back"
        PropertyChanges { target: flipRotation; angle: 180 }
        when: envelope.flipped
    }

    transitions: Transition {
        ParallelAnimation {
            SequentialAnimation {
                PropertyAnimation { target: envelope; to: 1.4; property: "scale"; duration: 300; easing.type: Easing.InCurve }
                PropertyAnimation { target: envelope; to: 1; property: "scale"; duration: 300; easing.type: Easing.InCurve }
            }
            RotationAnimation { target: flipRotation; property: "angle"; duration: 600; direction: RotationAnimation.Clockwise; easing.type: Easing.InOutCubic }
        }
    }
}
