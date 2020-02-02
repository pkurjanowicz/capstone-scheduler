<template>
    <div class="modal-backdrop">
        <div class="modal">
            <header class="modal-header">
                <button class='x-out-button' @click="close"> X </button>
            </header>
            <section class="modal-body">
                <slot name="body">
                <div>
                <h2>Your Groups:</h2>
                <br>
                <ul>
                <li v-for="items in groupInfo" v-bind:key="items">{{ items }}</li>
                </ul>
                </div>
                <h2>Create a New Group Below:</h2>
                <br>
                <label>Group Name:</label>
                <input v-model="groupName" v-on:keyup.enter="submitNewGroup"/>
                <br>
                <label>Group emails:</label>
                <input v-model="groupEmails" v-on:keyup.enter="submitNewGroup" 
                placeholder="Add comma separated emails..."/>
                
                <br>
                <button class="submit" @click="submitNewGroup">Submit</button>
                
                    
                    
                    
                    
                    
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
    props: ['userID', 'groupInfo', 'value'],
    data() {
        return {
            userID: '',
            groupName: '',
            groupEmails: '',
            
        }

    },
    components: {
        VueTags
    },
    
    methods: {
        submitNewGroup() {

            this.groupEmails.replace(',', '');
            axios.post('/newgroup', { owner_id: this.userID, group_name: this.groupName, emails: this.groupEmails })
            .then((response) => {
                this.groupName = ''
                this.groupEmails = ''
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