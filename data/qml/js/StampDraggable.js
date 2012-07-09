function checkStatus() {

    // check if the stamp has been dropped on the envelope
    // we require the full stamp to be within the envelope

    if ((x < envelope.front.x) || (y < envelope.front.y) ||
        (x + width > envelope.front.x + envelope.front.width) || (y + height > envelope.front.y + envelope.front.height)) {
        stamp.destroy(300)
        state = "shrunk"
        servicesModel.destroyStamp(stamp.serviceUid)
    }
    else {
        state = "normal"
    }
}
