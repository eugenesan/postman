var lastSpawn = null
var prevPoint = null

function createDraggable(mouse, stamp) {

    // store mouse position
    prevPoint = { "x": mouse.x, "y": mouse.y }

    // calculate mouse offset from top-left point
    var spawnPosition = stampPaletteItem.mapToItem(envelope.front, mouse.x, mouse.y)

    var component = Qt.createComponent("Stamp.qml")
    lastSpawn = component.createObject(envelope.front)

    lastSpawn.x = spawnPosition.x - lastSpawn.width / 2
    lastSpawn.y = spawnPosition.y - lastSpawn.width / 2
    lastSpawn.serviceName = stamp.serviceName
    lastSpawn.serviceIcon = stamp.serviceIcon
    lastSpawn.serviceUid = servicesModel.createStamp(stamp.serviceName)
    servicesModel.setSelectedStamp(lastSpawn.serviceUid)
}

function moveSpawn(mouse) {
    if (lastSpawn != null) {

        lastSpawn.x = lastSpawn.x + (mouse.x - prevPoint.x)
        lastSpawn.y = lastSpawn.y + (mouse.y - prevPoint.y)

        prevPoint = { "x": mouse.x, "y": mouse.y }
    }
}

function releaseSpawn() {
    if (lastSpawn != null) {
        lastSpawn.checkStatus()
        lastSpawn = null
    }
}

function createStamp(serviceName, serviceIcon) {

    var component = Qt.createComponent("Stamp.qml")
    var stamp = component.createObject(envelope.front)

    // calculate top-right corner of envelope
    var topRightPoint = { "x": envelope.front.width, "y": 0 }
    var stampCount = servicesModel.count()

    stamp.x = topRightPoint.x - stamp.width - 40 - (stamp.width + 20) * stampCount
    stamp.y = topRightPoint.y + 40
    stamp.state = "normal"
    stamp.serviceName = serviceName
    stamp.serviceIcon = serviceIcon
    stamp.serviceUid = servicesModel.createStamp(stamp.serviceName)
    servicesModel.setSelectedStamp(stamp.serviceUid)
}
