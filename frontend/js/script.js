new Vue({
    el: '#app',
    vuetify: new Vuetify(),
    data: () => ({
        type: 'month',
        types: ['month', 'week', 'day'],
        mode: 'stack',
        modes: ['stack', 'column'],
        weekday: [0, 1, 2, 3, 4, 5, 6],
        weekdays: [
            { text: 'Sun - Sat', value: [0, 1, 2, 3, 4, 5, 6] },
            { text: 'Mon - Sun', value: [1, 2, 3, 4, 5, 6, 0] },
            { text: 'Mon - Fri', value: [1, 2, 3, 4, 5] },
            { text: 'Mon, Wed, Fri', value: [1, 3, 5] },
        ],
        value: '',
        events: [],
        colors: ['blue', 'indigo', 'deep-purple', 'cyan', 'green', 'orange', 'grey darken-1'],
    }),
    methods: {
        getEvents ({ start, end }) {
            const events = []

            const min = new Date(`${start.date}T00:00:00`)
            const max = new Date(`${end.date}T23:59:59`)
            const days = (max.getTime() - min.getTime()) / 86400000

            // data get

            fetch("http://127.0.0.1:5000/api/tasks?datetime=2020-11-11")
                .then((response) => {
                    return response.json();
                }).then((data) => {
                    const tasks = data.tasks
                for (var i=0; i<data.tasks.length; i++) {
                    console.log(tasks[i].title)
                    console.log(tasks[i].datetime)
                    events.push({
                        name: tasks[i].title,
                        start: tasks[i].datetime,
                        color: this.colors[0],
                    })
                }
            });


            this.events = events
        },
        getEventColor (event) {
            return event.color
        },

    },
})