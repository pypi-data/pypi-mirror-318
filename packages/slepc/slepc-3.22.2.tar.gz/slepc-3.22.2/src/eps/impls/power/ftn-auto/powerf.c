#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* power.c */
/* Fortran interface file */

/*
* This file was generated automatically by bfort from the C source
* file.  
 */

#ifdef PETSC_USE_POINTER_CONVERSION
#if defined(__cplusplus)
extern "C" { 
#endif 
extern void *PetscToPointer(void*);
extern int PetscFromPointer(void *);
extern void PetscRmPointer(void*);
#if defined(__cplusplus)
} 
#endif 

#else

#define PetscToPointer(a) (a ? *(PetscFortranAddr *)(a) : 0)
#define PetscFromPointer(a) (PetscFortranAddr)(a)
#define PetscRmPointer(a)
#endif

#include "slepceps.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epspowersetshifttype_ EPSPOWERSETSHIFTTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epspowersetshifttype_ epspowersetshifttype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epspowergetshifttype_ EPSPOWERGETSHIFTTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epspowergetshifttype_ epspowergetshifttype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epspowersetnonlinear_ EPSPOWERSETNONLINEAR
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epspowersetnonlinear_ epspowersetnonlinear
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epspowergetnonlinear_ EPSPOWERGETNONLINEAR
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epspowergetnonlinear_ epspowergetnonlinear
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epspowersetupdate_ EPSPOWERSETUPDATE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epspowersetupdate_ epspowersetupdate
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epspowergetupdate_ EPSPOWERGETUPDATE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epspowergetupdate_ epspowergetupdate
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epspowersetsignnormalization_ EPSPOWERSETSIGNNORMALIZATION
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epspowersetsignnormalization_ epspowersetsignnormalization
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epspowergetsignnormalization_ EPSPOWERGETSIGNNORMALIZATION
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epspowergetsignnormalization_ epspowergetsignnormalization
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epspowersetsnes_ EPSPOWERSETSNES
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epspowersetsnes_ epspowersetsnes
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epspowergetsnes_ EPSPOWERGETSNES
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epspowergetsnes_ epspowergetsnes
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  epspowersetshifttype_(EPS eps,EPSPowerShiftType *shift, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSPowerSetShiftType(
	(EPS)PetscToPointer((eps) ),*shift);
}
SLEPC_EXTERN void  epspowergetshifttype_(EPS eps,EPSPowerShiftType *shift, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSPowerGetShiftType(
	(EPS)PetscToPointer((eps) ),shift);
}
SLEPC_EXTERN void  epspowersetnonlinear_(EPS eps,PetscBool *nonlinear, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSPowerSetNonlinear(
	(EPS)PetscToPointer((eps) ),*nonlinear);
}
SLEPC_EXTERN void  epspowergetnonlinear_(EPS eps,PetscBool *nonlinear, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSPowerGetNonlinear(
	(EPS)PetscToPointer((eps) ),nonlinear);
}
SLEPC_EXTERN void  epspowersetupdate_(EPS eps,PetscBool *update, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSPowerSetUpdate(
	(EPS)PetscToPointer((eps) ),*update);
}
SLEPC_EXTERN void  epspowergetupdate_(EPS eps,PetscBool *update, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSPowerGetUpdate(
	(EPS)PetscToPointer((eps) ),update);
}
SLEPC_EXTERN void  epspowersetsignnormalization_(EPS eps,PetscBool *sign_normalization, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSPowerSetSignNormalization(
	(EPS)PetscToPointer((eps) ),*sign_normalization);
}
SLEPC_EXTERN void  epspowergetsignnormalization_(EPS eps,PetscBool *sign_normalization, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSPowerGetSignNormalization(
	(EPS)PetscToPointer((eps) ),sign_normalization);
}
SLEPC_EXTERN void  epspowersetsnes_(EPS eps,SNES snes, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
CHKFORTRANNULLOBJECT(snes);
*ierr = EPSPowerSetSNES(
	(EPS)PetscToPointer((eps) ),
	(SNES)PetscToPointer((snes) ));
}
SLEPC_EXTERN void  epspowergetsnes_(EPS eps,SNES *snes, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
PetscBool snes_null = !*(void**) snes ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(snes);
*ierr = EPSPowerGetSNES(
	(EPS)PetscToPointer((eps) ),snes);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! snes_null && !*(void**) snes) * (void **) snes = (void *)-2;
}
#if defined(__cplusplus)
}
#endif
