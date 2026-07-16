use skyline::{self, libc::{c_long, c_longlong, c_uint, c_ulong, c_ushort, uintmax_t}};
use core::ffi::c_void;

// Have to use the offsets since 2.1.0 has no symbol table
// Function Address - 0x7100000000 (Default Base Address) = Offset
// Use #[skyline::hook(offset = 0x842a0, inline)] to only change that line
#[skyline::main(name = "Testudo")]
pub fn main() {
    skyline::install_hooks!(
        buildWeaponHook
    );
}

// Forces this function to always return false when checking if a NG+ blade can make a weapon. (Allowing them to make a weapon)
// bool gf::GfMenuObjUtil::isBladeNoBuildWeapon(uint param_1)
#[skyline::hook(offset = 0x491048)]
fn buildWeaponHook(_p1: c_uint) -> bool{
    println!("[Randomizer] Allowed NG+ Blade ID {_p1} to Build Weapon");
    return false;
}