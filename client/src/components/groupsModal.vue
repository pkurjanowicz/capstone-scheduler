<template>
    <div class="modal-backdrop">
        <div class="modal">
            <header class="modal-header">
                <button class='x-out-button' @click="close"> X </button>
            </header>
            <section class="modal-body">
                <slot name="body">
                <div>
                <p>{{ groupTitle }}</p>
                </div>
                <label>Group Name:</label>
                <input v-model="groupName" v-on:keyup.enter="submitNewGroup"/>
                <br>
                <label>Create your group with emails:</label>
                <input v-model="groupEmails" v-on:keyup.enter="submitNewGroup"/>
                
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
    props: ['userID', 'groupTitle', 'value'],
    data() {
        return {
            userID: '',
            emails: [],
            groupName: '',
            groupEmails: '',
            
        }

    },
    components: {
        VueTags
    },
    
    methods: {
        submitNewGroup() {

            let previousIndex = 0; 
            let i = 0;
            let separated = '';
 
            for(i = 0; i < this.groupEmails.length; i++) { 
 
                if (this.groupEmails[i] == ', ') { 
    
                separated = this.groupEmails.slice(previousIndex, i); 
                this.emails.push(separated); 
                previousIndex = i + 1; 
                } 
            } 
 
            this.emails.push(this.groupEmails.slice(previousIndex, i)); 

            
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