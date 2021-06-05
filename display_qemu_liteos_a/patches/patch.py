import shutil
import sys
import os

if __name__ == '__main__':
    if len(sys.argv) > 1:
        root_dir = sys.argv[1]
        root_dir = os.path.join(os.getcwd(), root_dir)
        shutil.copy(os.path.join(root_dir, "vendor/ohos/display_qemu_liteos_a/patches/kernel_BUILD.gn"),
                    os.path.join(root_dir, "kernel/liteos_a/BUILD.gn"))
        shutil.copy(os.path.join(root_dir, "vendor/ohos/display_qemu_liteos_a/patches/build.sh"),
                    os.path.join(root_dir, "device/qemu/arm_virt/build/build.sh"))
        shutil.copy(os.path.join(root_dir, "vendor/ohos/display_qemu_liteos_a/patches/BUILD.gn"),
                    os.path.join(root_dir, "device/qemu/arm_virt/BUILD.gn"))
        shutil.copy(os.path.join(root_dir, "device/hisilicon/drivers/libs/ohos/llvm/hi3518ev300/libmtd_common.a"), 
                    os.path.join(root_dir, "device/qemu/drivers/libs/virt/"))
        shutil.copy(os.path.join(root_dir, "vendor/ohos/display_qemu_liteos_a/patches/qemu-init"), root_dir)
        shutil.copy(os.path.join(root_dir, "vendor/ohos/display_qemu_liteos_a/patches/qemu-run"), root_dir)

