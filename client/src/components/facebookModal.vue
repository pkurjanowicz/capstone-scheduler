<template>
    <div class="modal-backdrop">
        <div class="modal">
            <header class="modal-header">
                <button class='x-out-button' @click="close"> X </button>
            </header>
            <section class="modal-body">
                <slot name="body">
                    <div>
                        <label>Facebook Event URL:</label>
                        <input v-model="facebookURL" type="text"/>
                        <button class="button" @click="submitFacebookEvents">Submit</button>
                    </div>
                </slot>
            </section>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
let moment = require('moment');
export default {
    name: "facebookModal",
    props: ['userID', 'eventsList'],
    data(){
        return{
            facebookURL: '',
            facebookTitle: '',
            facebookStartTime: '',
            facebookEndTime: '',
            facebookDescription: '',
            facebookEvent: false,
            fbStartDate: '',
            fbEndDate: ''
        }
    },
    methods: {
        close() {
            this.$emit('close');
        },
        submitFacebookEvents(){
            'use strict';
 
            const ical = require('ical');
            let corsURL = 'https://cors-anywhere.herokuapp.com/' + this.facebookURL;

            ical.fromURL(corsURL, {}, (err, data) => {
                for (let k in data) {
                    if (data.hasOwnProperty(k)) {
                        var ev = data[k];
                        // console.log(ev);
                        if (data[k].type == 'VEVENT') {
                            console.log(data[k]);
                            this.fbStartDate = ev.start;
                            this.fbEndDate = ev.end;
                            this.facebookTitle = ev.summary;
                            this.facebookStartTime = this.fbStartDate;
                            // Sets start time to UTC
                            let fbEventStartDate = moment.utc(this.fbStartDate)
                            this.fbStartDate = fbEventStartDate.toISOString()
                            this.fbStartDate = fbEventStartDate.format("YYYY-MM-DD HH:mm:ss")

                            this.facebookEndTime = this.fbEndDate;
                            // Sets end time to UTC.
                            let fbEventEndDate = moment.utc(this.fbEndDate)
                            this.fbEndDate = fbEventEndDate.toISOString()
                            this.fbEndDate = fbEventEndDate.format("YYYY-MM-DD HH:mm:ss")

                            this.facebookDescription = ev.description;
                            this.facebookEvent = true;
                            this.dragEvent = false
                            axios.post('/newevent', { owner_id: this.userID, event_name: this.facebookTitle, event_details: this.facebookDescription, event_start_time: this.fbStartDate, event_end_time: this.fbEndDate, all_day: false, drag: false})

                            .then(() => {
                                this.getEvents()
                            });
                        }
                    }
                }
            });

            
        },
        addFacebookEventToDatabase(){
            

            

            
        }
        
    }
}
</script>

<style scoped>

</style>