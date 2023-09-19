# UE4 Stamina & Health System

A set of Blueprint assets for Unreal Engine 4 that give you basic health and stamina without buying something off the Marketplace.

Run and jump cost stamina. Stamina comes back after you stop burning it. Take damage and you lose health; that also regens if you wait a bit. When health hits zero, you get a death screen. There are HUD widgets for bars and numbers, plus a blood-on-screen effect when you're hurt.

## What's in here

These are `.uasset` files only — no project file. Drop them into your own UE4 project's `Content` folder (something like `Content/StaminaHealthSystem/` works fine).

| File | What it does |
|------|----------------|
| `HealthSystem` | Damage, regen, death, triggers blood overlay |
| `StaminaSystem` | Drain on run/jump, regen over time |
| `CharacterMovementSystem` | Hooks sprint and jump to stamina |
| `HealthHUD` / `StaminaHUD` | On-screen bars and numbers |
| `BloodMarks` | Red vignette that gets worse as health drops |
| `DeathMenu` | Screen when you die |
| `health_hud_icon` / `stamina_hud_icon` | Icons for the HUD |

Built around UE 4.12. Newer 4.x versions might need you to open and re-save the assets once.

## Getting started

1. Open your UE4 project (first-person template is a common starting point).
2. Copy every `.uasset` from this folder into `Content`.
3. Restart the editor if things look broken. **Fix Up Redirectors** if it asks.
4. If something won't load, try migrating or re-saving the asset for your engine version.

## Hooking it up to your character

You'll want a player character Blueprint. This is the rough order that works:

**Add the components** — `HealthSystem`, `StaminaSystem`, and `CharacterMovementSystem` on the character. Initialize them on `BeginPlay` (or wherever you set up the pawn).

**Show the HUD** — Create `HealthHUD`, `StaminaHUD`, and `BloodMarks` as widgets and add them to the viewport from the player controller. The health system can drive the blood overlay through `AddBloodMarks` when you take hits.

**Wire your inputs** — Run goes through the movement system and stamina. Jump costs stamina too. You can't aim while sprinting — block or ignore aim input when `bIsRunning` is true. On tick, let regen and HUD updates run (`GetHealthAmount`, `GetStaminaAmount` are the ones you'll call from the widgets). When something should hurt the player, call `DecreaseHealth` on the health component.

**Death** — At zero health, `HealthSystem` handles the death flow: show `DeathMenu`, hide the normal HUD and first-person mesh like the Blueprints are already set up to do.

Open any of the Blueprints in the editor if you want to tweak max values, regen delay, walk/sprint speed, bar colors, or how strong the blood effect is.

## Files

```
HealthSystem.uasset
StaminaSystem.uasset
CharacterMovementSystem.uasset
HealthHUD.uasset
StaminaHUD.uasset
BloodMarks.uasset
DeathMenu.uasset
health_hud_icon.uasset
stamina_hud_icon.uasset
LICENSE
README.md
```

- Handle missing optional field in the response without raising

- Support optional config file path via env var for easier deployment

- Support optional config file path via env var for easier deployment

- Fix the test that was flaky due to reliance on system time

- Correct the default value for the feature flag in production

- Improve the startup time by lazy-loading the heavy modules

- Bump the library version and pin the dependency in requirements

- Clean up leftover code from the previous implementation

- Remove the feature flag now that the feature is fully rolled out

- Support passing secrets via a separate file for security
