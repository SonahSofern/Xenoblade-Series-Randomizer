use skyline::{self, install_hooks, libc::{c_long, c_uchar, c_ushort}};
use core::ffi::c_void;
use std::mem::transmute;

// XCDE
// getTutorial returning doesnt progress the flags
// _ZNK4game23MenuFacadeFullscreenTop14isOpenTutorialEv Checks every frame if a tutorial is open


extern "C" {
    fn _ZN4game15MenuSeqTutorialC1EPNS_17MenuSeqCommonBaseEtNS_21MenuPartsTutorialPage8ViewModeE(_this_ptr: *mut c_void, _sthis_ptr: *mut c_void, _16: u16, _32: u32);
    fn _ZN4game8DataUtil15setTutorialViewERKN2fw8DocumentEtb(_this_ptr: *mut c_void, _short: c_ushort, _bool: bool);
    fn _ZN4game15TutorialManager6updateERKN2fw10UpdateInfoE(this: *mut u8, update_info: *mut u8);
    fn _ZN4game8DataUtil11setTutorialERKN2fw8DocumentEtbb(this: *mut c_void, p2: u16, p3: bool, p4: bool);
    fn _ZN4game8DataUtil11getTutorialERKN2fw8DocumentEt(this: *mut c_void, p2: u16, p3: bool, p4: bool);
    fn _ZN4game15MenuSeqTutorial5closeEv(this: *mut c_void);    
    fn _ZN4game15MenuSeqTutorial7onEnterERKNS_22MenuSequenceEnterParamE(this: *mut c_void); 
    fn _ZNK4game19MenuEventDispatcher3setINS_13menu_tutorial12MenuCloseAllEEEmRKT_(this: *mut c_void, this2: *mut c_void);
    fn _ZN4game12TutorialUtil5forceERKN2fw8DocumentEh();
    
}

#[skyline::main(name = "Testudo")]
pub fn main() {
    install_hooks!(
        testHook3
    );
}


 // This showed every tutorial repeatedly, you would just be clicking a through all 20 of them
#[skyline::hook(replace = _ZN4game8DataUtil11getTutorialERKN2fw8DocumentEt)]
fn testHook3(_this_ptr: *mut c_void, _short: c_ushort, _bool: bool) -> bool{
    // Every time getTutorial is called it immediately calls setTutorial, which sets the flag as though the tutorial was seen
    unsafe {
        _ZN4game8DataUtil11setTutorialERKN2fw8DocumentEtbb(_this_ptr, _short, true, false);
    }
    true
}

// Game freezes (not crashes)
#[skyline::hook(replace = _ZN4game12TutorialUtil5forceERKN2fw8DocumentEh)] 
fn tutHook(_this_ptr: *mut c_void, _p2: c_uchar){
    println!("tutHook");
}
// Look into recieve input MenuSeqTutorial::receiveInput
// 

// Game freezes (not crashes)
#[skyline::hook(replace = _ZN4game15MenuSeqTutorial7onEnterERKNS_22MenuSequenceEnterParamE)] 
fn onEnterHook(_this_ptr: *mut c_void) -> u64{
    println!("onEnterHook");
    return 0;
}
 
// Only worked during the menu where you revisit tutorials, it triggers when you close it not causing the close itself 0x462c80 doesnt work either
// #[skyline::hook(offset = 0x462b20)] 
// fn instaHook(p1: c_long){
//     println!("InstaCloseHook");
//     unsafe {
//         // 1. Convert c_long into a raw byte pointer so we can do pointer arithmetic
//         let param_1_ptr = p1 as *mut u8;

//         if !param_1_ptr.is_null() {
//             // 2. Go to offset 0x18 and read the 64-bit pointer stored there (*mut c_void)
//             // This mirrors Ghidra's: *(MenuSeqCommonBase **)(param_1 + 0x18)
//             let tutorial_class_ptr = *(param_1_ptr.add(0x18) as *mut *mut c_void);

//             if !tutorial_class_ptr.is_null() {
//                 println!("[Mod] Found Tutorial Class Pointer: {:p}. Forcing close!", tutorial_class_ptr);
                
//                 // 3. Pass the correct pointer to the game's official close function
//                 _ZN4game15MenuSeqTutorial5closeEv(tutorial_class_ptr);
//             }
//         }
//     }
// }

#[skyline::hook(replace = _ZN4game15MenuSeqTutorialC1EPNS_17MenuSeqCommonBaseEtNS_21MenuPartsTutorialPage8ViewModeE)] // Runs during intro tutorials seems to be related to the UI
fn testHook(_this_ptr: *mut c_void, _sthis_ptr: *mut c_void, _16: u16, _32: u32){
    println!("_ZN4game15MenuSeqTutorialC1EPNS_17MenuSeqCommonBaseEtNS_21MenuPartsTutorialPage8ViewModeE");
    call_original!(_this_ptr, _sthis_ptr, _16, _32);
}

// Runs when viewing tutorials in field and menu
#[skyline::hook(replace = _ZN4game8DataUtil15setTutorialViewERKN2fw8DocumentEtb)]
fn testHook2(_this_ptr: *mut c_void, _short: c_ushort, _bool: bool){
    println!("_ZN4game8DataUtil15setTutorialViewERKN2fw8DocumentEtb");
    call_original!(_this_ptr, _short, _bool);
}


#[skyline::hook(replace = _ZN4game8DataUtil11setTutorialERKN2fw8DocumentEtbb)]
fn setTutorialHook(_this_ptr: *mut c_void, _short: c_ushort, _bool: bool,_bool2: bool){
    call_original!(_this_ptr, _short, true, false);
    println!("setTutorial Hook");
}