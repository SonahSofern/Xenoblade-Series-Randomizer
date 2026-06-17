use skyline::{self, install_hooks, libc::{c_long, c_uchar, c_ushort}};
use core::ffi::c_void;
use std::mem::transmute;

// XCDE

extern "C" {
    fn _ZN4game8DataUtil11setTutorialERKN2fw8DocumentEtbb(_p1: *mut c_void, p2: u16, p3: bool, p4: bool);
    fn _ZN4game8DataUtil11getTutorialERKN2fw8DocumentEt(_p1: *mut c_void, p2: u16, p3: bool, p4: bool);
}

#[skyline::main(name = "XCDE")]
pub fn main() {
    install_hooks!(
        skipTutorialHook
    );
}

#[skyline::hook(replace = _ZN4game8DataUtil11getTutorialERKN2fw8DocumentEt)]
fn skipTutorialHook(_ptr: *mut c_void, _short: c_ushort, _bool: bool) -> bool{
    unsafe {
        if (!call_original!(_ptr, _short, _bool)){ // call getTutorial and if one exists then we call setTutorial immediately
            // Params true, false lead to the tutorial not being shown, gotten from void __thiscall game::DevGuiFlag::buildMpguiMessage(DevGuiFlag *this,MpguiContext *param_1)
            // This was a debug function that turned off tutorials for testing
            println!("[Randomizer] Skipped Tutorial ID (MNU_ttrl): {_short}");
            _ZN4game8DataUtil11setTutorialERKN2fw8DocumentEtbb(_ptr, _short, true, false); 
        } 
    }
    true 
}