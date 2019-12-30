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
                <input-tags v-model="emails">
                  
                    <div class="emails-input"
                        slot-scope="{tag,removeTag,inputEventHandlers,inputBindings }">
                        <div v-for="(email, index) in emails"
                        :key='index'
                        class="tags-input-email">
                        <span>{{ email }}</span>
                        <button type="button" class="tags-input-remove"
                            v-on:click="removeTag(email)"
                        >&times;
                        </button>
                        </div>
                        <input
                        class="email-input-text"  placeholder="Add invitee email..."
                        v-on="inputEventHandlers"
                        v-bind="inputBindings"
                        >
                        <br>
                        <button class="submit" @click="submitNewGroup">Submit</button>
                    </div>
                    
                    </input-tags>
                    
                    
                    
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
    props: ['userID', 'groupName', 'value'],
    methods: {
        submitNewGroup() {
            
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