<template>
    <div class="modal-backdrop">
        <div class="modal">
            <header class="modal-header">
                <button class='x-out-button' @click="close"> X </button>
            </header>
            <section class="modal-body">
                <slot name="body">
                <label>Group Name:</label>
                <input v-model="groupName" v-on:keyup.enter="submitNewGroup"/>
                <br>
                <label>Create your group with emails:</label>
                <input v-model="emails" separator="," maximum="5" 
                placeholder="Just enter some emails separated by a comma">
                <br>
                <button class="submit" @click="submitNewGroup">Submit</button>
                <!--
                <div>
                <p v-for="(email, index) in emails" v-bind:key="index">{{ email }}</p>
                
                </div>
                -->
                </slot>
            </section>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import VueTags from "vue-tags"

let moment = require('moment')

export default {
    name: "groupsModal",
    data() {
        return {
            userID: '',
            emails: [],
            groupName: '',
            
        }

    },
    components: {
        VueTags
    },
    props: ['userID', 'groupName', 'value', 'separator', 'tags'],
    methods: {
        submitNewGroup(tags, separator) {

            for (let tag of tags) {
                this.emails.push(tag + separator);
            }

            this.emails.join(" ").slice(0, -1);


            
            axios.post('/newgroup', { owner_id: this.userID, group_name: this.groupName, emails: this.emails })
            .then((response) => {
                this.groupName = ''
                this.emails = ''
                this.currentGroupId = response.data.group_id
                this.close()
                
             })

        },

        close() {
        this.$emit('close');
        },
        
    }
}
</script>

<style scoped>

</style>