<template>
    <div class="modal-backdrop">
        <div class="modal">
            <header class="modal-header">
                <button class='x-out-button' @click="close"> X </button>
            </header>
            <section class="modal-body">
                <slot name="body">
                    <div>
                        <p>Here is the title:<br> {{ title }}</p><br><br>
                        <p>Here are the details:<br> {{ details }}</p>
                        <p> here is the start: {{start}}</p>
                        <p> Here is the end: {{end}}</p>
                        <p v-for='(invite, index) in invites' :key='index'> email:{{invite.email}} {{invite.accepted}}</p>
                    </div>
                </slot>
            </section>
        </div>
    </div>
</template>

<script>
export default {
    name: "eventDetailsModal",
    props: ['title', 'details','start','end', 'invites'],
    methods: {
        close() {
        this.$emit('close');
        },
    }
}
</script>

<style scoped>

</style>