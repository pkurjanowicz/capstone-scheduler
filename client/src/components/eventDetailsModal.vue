<template>
    <div class="modal-backdrop">
        <div class="modal">
            <header class="modal-header">
                <button class='x-out-button' @click="close"> X </button>
            </header>
            <section class="modal-body">
                <slot name="body">
                    <div>
                        {{ title }}
                        {{ details }}
                    </div>
                </slot>
            </section>
        </div>
    </div>
</template>

<script>
export default {
    name: "eventDetailsModal",
    props: ['title', 'details'],
    methods: {
        close() {
        this.$emit('close');
      },
    }
}
</script>

<style scoped>
.modal-backdrop {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
}

.modal {
    background: #FFFFFF;
    box-shadow: 2px 2px 20px 1px;
    overflow-x: auto;
    display: flex;
    flex-direction: column;
    height: 200px;
    width: 200px;
}

.modal-header {
    padding: 20px 20px 0 20px;
    display: flex;
}

.x-out-button {
    margin-left: auto;
    order: 2;
}
</style>