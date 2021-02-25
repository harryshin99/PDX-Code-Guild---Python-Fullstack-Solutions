let app = new Vue({
    el: '#app',
    data: {
        hour: '',
        minute: '',
        second: '',
        meridian: '',
        notInitiated: true,
        startTimer: '',
    },
    methods: {
        stopWatch: function() {
            this.notInitiated = false;
            this.startTimer = new Date();
            setInterval(function() {
                app.startTimer.setHours(0,0,0,0)
            }, 100);
        }
    },
    created: function() {
        // startClock();
        setInterval(function() {
            [app.hour, app.minute, app.second, app.meridian] = new Date().toLocaleTimeString("en-US").split(/:| /);
            // app.currentTime = new Date();
        }, 1000);
    }
})